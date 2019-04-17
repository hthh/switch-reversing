import struct
import sys
import re
import bisect
import hashlib
import time
from functools import partial
from collections import defaultdict
from unicorn import *
from unicorn.arm64_const import *
from capstone import *

import nxo64
from demangling import get_demangled
from unicornhelpers import load_nxo_to_unicorn, create_unicorn_arm64

from hashes import all_hashes_300
from hashes_gen import all_hashes
from data610 import data610 as reference_data

#reference_data = {}
#all_hashes = {}
#all_hashes_300 = {}


ONLY_FUNCTION = None

DEFAULT_LOAD_BASE = 0x7100000000

def demangle(s):
    value = get_demangled(s)
    pre = 'nn::sf::cmif::server::detail::CmifProcessFunctionTableGetter<'
    post = ', void>::s_Table'
    if value.startswith(pre) and value.endswith(post):
        value = value[len(pre):-len(post)]
    return value


class MemoryChunk(object):
    def __init__(self, name, base, size):
        self.base = base
        self.size = size

    @property
    def end(self):
        return self.base + self.size

    def __repr__(self):
        return 'MemoryChunk(name=%r, base=0x%X, size=0x%X)' % (self.name, self.base, self.size)

class AllocatingChunk(MemoryChunk):
    def __init__(self, name, base, size):
        super(AllocatingChunk, self).__init__(name, base, size)
        self.reset()

    def reset(self):
        self._next_ptr = self.base
        self.bytes_allocated = 0

    def alloc(self, size):
        available = self.end - self._next_ptr
        assert available > 0
        allocation_size = (size + 0xF) & ~0xF
        if allocation_size > available:
            raise Exception('Could not allocate 0x%X bytes from AllocatingChunk %r' % size, self.name)
        result = self._next_ptr
        self._next_ptr += allocation_size
        self.bytes_allocated += size
        return result

    def __repr__(self):
        return 'MemoryChunk(name=%r, base=0x%X, size=0x%X)' % (self.name, self.base, self.size)

class Nx64Simulator(object):
    def __init__(self, nxo, stack_size=0x2000, host_heap_size=0x100000, runtime_heap_size=0x2000, loadbase=DEFAULT_LOAD_BASE, trace_instructions=False):
        self.uc = create_unicorn_arm64()
        self.cs = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
        self.loadbase = loadbase
        load_nxo_to_unicorn(self.uc, nxo, loadbase)

        self._last_chunk_base = 0
        self._chunk_step = 0x100000000
        self._chunks = []

        self.stack = self.create_chunk('stack', stack_size)
        self.host_heap = self.create_chunk('host_heap', host_heap_size, AllocatingChunk)
        self.runtime_heap = self.create_chunk('runtime_heap', runtime_heap_size, AllocatingChunk)
        self.function_pointer_chunk = self.create_chunk('function_pointers', 0)
        self.next_function_pointer = self.function_pointer_chunk.base

        self._data_for_reset = []

        self.current_trace = None

        self._hook_functions = {}

        self.return_pointer = self.create_trace_function_pointer(self.on_return_hook_function)

        self.trace_instructions = trace_instructions

        self.trace_instruction_hooks = []

    def on_return_hook_function(self, uc):
        #print 'on_return_hook_function'
        return False

    def create_trace_function_pointer(self, func):
        function_pointer = self.next_function_pointer
        self.next_function_pointer += 8

        self._hook_functions[function_pointer] = func
        return function_pointer

    def create_chunk(self, name, size, cls=MemoryChunk):
        base = self._last_chunk_base + self._chunk_step
        chunk = cls(name, base, size)
        if size:
            self.uc.mem_map(base, size)
        self._last_chunk_base = base
        return chunk

    def load_host_data(self, data, reset=False):
        p = self.host_heap.alloc(len(data))
        self.uc.mem_write(p, data)
        if reset:
            self._data_for_reset.append((p, data))
        return p

    def dump_regs():
        values = []
        for i in range(28):
            values.append(('X%d' % i, self.uc.reg_read(UC_ARM64_REG_X0+i)))
        values.append(('X29', self.uc.reg_read(UC_ARM64_REG_X29)))
        values.append(('X30', self.uc.reg_read(UC_ARM64_REG_X30)))
        values.append(('SP',  self.uc.reg_read(UC_ARM64_REG_SP)))
        values.append(('PC',  self.uc.reg_read(UC_ARM64_REG_PC)))
        print ', '.join('%s=%X' % i for i in values)

    def qword(self, addr):
        return struct.unpack('<Q', self.uc.mem_read(addr, 8))[0]

    def dword(self, addr):
        return struct.unpack('<I', self.uc.mem_read(addr, 4))[0]

    def sdword(self, addr):
        return struct.unpack('<i', self.uc.mem_read(addr, 4))[0]

    def write_qword(self, addr, value):
        self.uc.mem_write(addr, struct.pack('<Q', value))

    def write_dword(self, addr, value):
        self.uc.mem_write(addr, struct.pack('<I', value))

    def reset_host_data(self):
        for addr, data in self._data_for_reset:
            self.uc.mem_write(addr, data)

    def get_instruction(self, addr):
        instructions = list(self.cs.disasm(str(self.uc.mem_read(addr, 4)), addr))
        if instructions:
            assert len(instructions) == 1
            return instructions[0]
        return None

    def add_trace_instruction_hook(self, cb):
        self.trace_instruction_hooks.append(cb)

    def trace_call(self, funcptr, args, trace_object=None):
        if trace_object is None:
            trace_object = {}

        self.reset_host_data()

        register_args, stack_args = args[:8],  args[8:]

        for i, v in enumerate(register_args):
            self.uc.reg_write(UC_ARM64_REG_X0 + i, v)

        for i in xrange(len(register_args), 9):
            self.uc.reg_write(UC_ARM64_REG_X0 + i, 0)

        sp = self.stack.end
        if stack_args:
            stack_space = len(stack_args) * 8
            stack_space = (stack_space + 0xF) & ~0xF
            sp -= stack_space
            for i, v in enumerate(v):
                self.write_qword(sp + i * 8, v)

        self.uc.reg_write(UC_ARM64_REG_SP, sp)
        self.uc.reg_write(UC_ARM64_REG_PC, funcptr)

        self.uc.reg_write(UC_ARM64_REG_X30, self.return_pointer)

        assert self.current_trace is None
        self.current_trace = trace_object

        try:
            while True:
                try:
                    pc = self.uc.reg_read(UC_ARM64_REG_PC)
                    if self.trace_instruction_hooks or self.trace_instructions:
                        if self.trace_instruction_hooks:
                            instruction = self.get_instruction(pc)
                            for cb in self.trace_instruction_hooks:
                                cb(self.uc, instruction)
                        
                        if self.trace_instructions:
                            # TODO: this will trace strangely if trace_instruction_hooks changes PC
                            instruction = self.get_instruction(pc)
                            if instruction is not None:
                                print '0x%08x:    %s  %s' % (instruction.address, instruction.mnemonic, instruction.op_str)
                            else:
                                print '0x%08x:    [INVALID]' % (instruction.address,)

                        # trace_instruction_hooks may have changed PC
                        self.uc.emu_start(self.uc.reg_read(UC_ARM64_REG_PC), 0, count=1)
                    else:
                        self.uc.emu_start(pc, 0)
                except UcError as e:
                    pc = self.uc.reg_read(UC_ARM64_REG_PC)
                    if pc in self._hook_functions:
                        #print 'hook function for %X' % (pc,)
                        if self._hook_functions[pc](self.uc):
                            continue
                        else:
                            break

                    print 'UcError @ pc 0x%X' % (pc,)
                    print '', e
                    raise
        finally:
            self.trace_instruction_hooks = []
            self.current_trace = None

    def invoke_trace_method(self, method_name, *args, **kwargs):
        assert self.current_trace is not None
        try:
            method = getattr(self.current_trace, method_name)
        except AttributeError:
            raise NotImplementedError("Class %r does not implement %r" % (self.current_trace.__class__.__name__, method_name))
        return method(*args, **kwargs)



class IPCServerSimulator(Nx64Simulator):
    def __init__(self, nxo):
        super(IPCServerSimulator, self).__init__(nxo)
        self.ipc_magic = 0x49434653
        message_data = self._make_message_data(1600) + ('\x00' * 0x1000)
        self.message_ptr = self.load_host_data(message_data)

        message_struct_data = struct.pack('<QQ', self.message_ptr, len(message_data))
        self.message_struct_ptr = self.load_host_data(message_struct_data, reset=True)

        ipc_functions = [
            partial(self.invoke_trace_method, 'PrepareForProcess'),           # PrepareForProcess(nn::sf::cmif::CmifMessageMetaInfo const&)
            partial(self.invoke_trace_method, 'OverwriteClientProcessId'),    # OverwriteClientProcessId(ulong *)
            partial(self.invoke_trace_method, 'GetBuffers'),                  # GetBuffers(nn::sf::detail::PointerAndSize *)
            partial(self.invoke_trace_method, 'GetInNativeHandles'),          # GetInNativeHandles(nn::sf::NativeHandle *)
            partial(self.invoke_trace_method, 'GetInObjects'),                # GetInObjects(nn::sf::cmif::server::CmifServerObjectInfo *)
            partial(self.invoke_trace_method, 'BeginPreparingForReply'),      # BeginPreparingForReply(nn::sf::detail::PointerAndSize *)
            partial(self.invoke_trace_method, 'SetBuffers'),                  # SetBuffers(nn::sf::detail::PointerAndSize *)
            partial(self.invoke_trace_method, 'SetOutObjects'),               # SetOutObjects(nn::sf::cmif::server::CmifServerObjectInfo *)
            partial(self.invoke_trace_method, 'SetOutNativeHandles'),         # SetOutNativeHandles(nn::sf::NativeHandle *)
            partial(self.invoke_trace_method, 'BeginPreparingForErrorReply'), # BeginPreparingForErrorReply(nn::sf::detail::PointerAndSize *,ulong)
            partial(self.invoke_trace_method, 'EndPreparingForReply'),        # EndPreparingForReply(void)
        ]

        ipc_function_pointers = [self.create_trace_function_pointer(i) for i in ipc_functions]

        ipc_vtable_ptr = self.load_host_data(struct.pack('<' + 'Q' * len(ipc_function_pointers), *ipc_function_pointers))
        self.ipc_object_ptr = self.load_host_data(struct.pack('<QQ', ipc_vtable_ptr, 0))


        target_functions = [partial(self.invoke_trace_method, 'target_function', i*8) for i in range(512)]
        target_function_pointers = [self.create_trace_function_pointer(i) for i in target_functions]

        target_vtable_ptr = self.load_host_data(struct.pack('<' + 'Q' * len(target_function_pointers), *target_function_pointers))
        self.target_object_ptr = self.load_host_data(struct.pack('<QQ', target_vtable_ptr, 0))

        ret_instruction_ptr = self.load_host_data(struct.pack('<I', 0xd65f03c0))
        in_object_vtable_ptr = self.load_host_data(struct.pack('<Q', ret_instruction_ptr) * 16)
        self.in_object_ptr = self.load_host_data(struct.pack('<Q', in_object_vtable_ptr) + '\0' * (8*16))

        self.buffer_memory = self.load_host_data('\x00' * 0x1000)
        self.output_memory = self.load_host_data('\x00' * 0x1000)


    def _make_message_data(self, cmd_id):
        ipc_magic = 0x49434653
        return struct.pack('<QQ', ipc_magic, cmd_id)


    def trace_cmd_impl(self, dispatch_func, cmd_id):
        # Some commands have in-dispatcher validation. If we fail this
        # validation we miss some information about vtable offsets and
        # returned objects. This tries to brute-force until we find an
        # input that passes that validation.

        trace = self.try_trace_cmd(dispatch_func, cmd_id, struct.pack('<QQQQQQ', 0, 0, 0, 0, 0, 0))
        if trace.is_correct():
            return trace

        # Pass checks for non-zero inline data
        trace = self.try_trace_cmd(dispatch_func, cmd_id, struct.pack('<QQQQQQ', 1, 1, 1, 1, 1, 1))
        if trace.is_correct():
            return trace

        # Pass buffer size checks
        buffer_sizes = [128, 33, 1]
        for buffer_size in buffer_sizes:
            trace = self.try_trace_cmd(dispatch_func, cmd_id, struct.pack('<QQQQ', 0, 0, 0, 0), buffer_size=buffer_size)
            if trace.is_correct():
                return trace

        # Pass checks for buffer size, and non-zero inline data
        for buffer_size in buffer_sizes:
            trace = self.try_trace_cmd(dispatch_func, cmd_id, struct.pack('<QQQQ', 1, 1, 1, 1), buffer_size=buffer_size)
            if trace.is_correct():
                return trace

        sys.stderr.write('Warning: unable to brute-force validation on dispatch_func %X command %d\n' % (dispatch_func, cmd_id))
        return trace # oh well

    def trace_cmd(self, dispatch_func, cmd_id):
        trace = self.trace_cmd_impl(dispatch_func, cmd_id)
        if trace.description is None:
            trace = self.try_trace_cmd(dispatch_func, cmd_id, struct.pack('<QQQQQQ', 0, 0, 0, 0, 0, 0), trace_branches=True)
        return trace


    def try_trace_cmd(self, dispatch_func, cmd_id, data, **kwargs):
        self.uc.mem_write(self.message_ptr, self._make_message_data(cmd_id) + data)
        trace = IPCServerTrace(self, dispatch_func, cmd_id, **kwargs)
        self.trace_call(dispatch_func, [self.target_object_ptr, self.ipc_object_ptr, self.message_struct_ptr], trace)
        return trace


UC_REG_BY_NAME = {
    "x0": UC_ARM64_REG_X0,
    "x1": UC_ARM64_REG_X1,
    "x2": UC_ARM64_REG_X2,
    "x3": UC_ARM64_REG_X3,
    "x4": UC_ARM64_REG_X4,
    "x5": UC_ARM64_REG_X5,
    "x6": UC_ARM64_REG_X6,
    "x7": UC_ARM64_REG_X7,
    "x8": UC_ARM64_REG_X8,
    "x9": UC_ARM64_REG_X9,
    "x10": UC_ARM64_REG_X10,
    "x23": UC_ARM64_REG_X23,
    "x24": UC_ARM64_REG_X24,
    "x25": UC_ARM64_REG_X25,
}


VERBOSE_COMMAND = None
#VERBOSE_COMMAND = 0

class BranchTracer(object):
    def __init__(self, simulator, cmd_id):
        self.loaded_cmd_id = False
        self.stopped = False
        self._simulator = simulator
        self.taints = set()
        self.cmp_with = None
        self.cmd_id = cmd_id
        self.range_top = 0xFFFFFFFF
        self.switch_top = None
        self.switch_stride = None
        self.taint_offsets = {}
        self.taint_rors = {}
        self.cmp_ror = 0
        self.cmp_lhs = 0
        #print 'TRACING %d' % cmd_id

    def trace_instruction(self, uc, instruction):
        verbose = True # (VERBOSE_COMMAND is not None and self.cmd_id == VERBOSE_COMMAND)
        verbose = False
        if self.stopped: return
        if not self.loaded_cmd_id:
            if instruction.mnemonic != 'ldr' or not instruction.op_str.endswith(', #8]'):
                return
            # TODO: is the offset always in the instruction?
            tainted, base = instruction.op_str[:-len(', #8]')].split(', [')
            if not base.startswith('x') or not tainted.startswith('w'):
                return
            if uc.reg_read(UC_REG_BY_NAME[base]) != self._simulator.message_ptr:
                return
            if verbose: print 'BranchTracer start'
            if verbose: print '0x%08x:    %s  %s' % (instruction.address, instruction.mnemonic, instruction.op_str)
            #print '\t%X\t%X' % (uc.reg_read(UC_REG_BY_NAME[base]), self._simulator.message_ptr)

            self.loaded_cmd_id = True
            self.taints.add(int(tainted[1:]))
            self.taint_offsets[int(tainted[1:])] = 0
            self.taint_rors[int(tainted[1:])] = 0
            #print self.taints
            return

        parts = instruction.op_str.replace(',', ' ').replace('[', ' ').replace(']', ' ').split()

        if any(('w%d'%i) in parts for i in self.taints) or any(('x%d'%i) in parts for i in self.taints):
            if verbose: print '*',
        else:
            if verbose: print ' ',
        if verbose: print '0x%08x:    %s  %s' % (instruction.address, instruction.mnemonic, instruction.op_str)

        if instruction.mnemonic == 'mov' and parts[0].startswith('w') and parts[1].startswith('w') and parts[1] != 'wzr' and int(parts[1][1:]) in self.taints:
            new_taint = int(parts[0][1:])
            self.taints.add(new_taint)
            self.taint_offsets[new_taint] = self.taint_offsets[int(parts[1][1:])]
            self.taint_rors[new_taint] = self.taint_rors[int(parts[1][1:])]
            if verbose: print '\ttainted x%d' % new_taint

        if instruction.mnemonic == 'sub' and parts[0].startswith('w') and parts[1].startswith('w') and parts[1] != 'wzr' and int(parts[1][1:]) in self.taints:
            if parts[2].startswith('#'):
                new_taint = int(parts[0][1:])
                self.taints.add(new_taint)
                self.taint_offsets[new_taint] = self.taint_offsets[int(parts[1][1:])] - int(parts[2][1:], 16)
                self.taint_rors[new_taint] = self.taint_rors[int(parts[1][1:])]
                if verbose: print '\ttainted (sub) x%d' % new_taint

        if instruction.mnemonic == 'ror' and parts[0].startswith('w') and parts[1].startswith('w') and parts[1] != 'wzr' and int(parts[1][1:]) in self.taints:
            if parts[2].startswith('#'):
                new_taint = int(parts[0][1:])
                self.taints.add(new_taint)
                self.taint_offsets[new_taint] = self.taint_offsets[int(parts[1][1:])]
                self.taint_rors[new_taint] = self.taint_rors[int(parts[1][1:])] + int(parts[2][1:], 16)
                if verbose: print '\ttainted (ror) x%d' % new_taint

        if instruction.mnemonic == 'add' and parts[0].startswith('w') and parts[1].startswith('w') and int(parts[1][1:]) in self.taints:
            if parts[2].startswith('w'):
                new_taint = int(parts[0][1:])
                value = uc.reg_read(UC_REG_BY_NAME['x' + parts[2][1:]])
                value &= 0xFFFFFFFF
                value -= (value & 0x80000000) * 2
                if verbose: print '\tvalue:', value
                self.taints.add(new_taint)
                self.taint_offsets[new_taint] = self.taint_offsets[int(parts[1][1:])] + value
                self.taint_rors[new_taint] = self.taint_rors[int(parts[1][1:])]
                if verbose: print '\ttainted (add) x%d' % new_taint

        if instruction.mnemonic == 'cmp':
            self.cmp_with = None
            if parts[0].startswith(('w', 'x')) and int(parts[0][1:]) in self.taints:
                if parts[1].startswith('#'):
                    if verbose: print '\tcmp_with %r' % instruction.op_str
                    self.cmp_with = int(parts[1][1:], 16)
                    self.cmp_delta = self.taint_offsets[int(parts[0][1:])]
                    self.cmp_ror = self.taint_rors[int(parts[0][1:])]
                    self.cmp_lhs = uc.reg_read(UC_REG_BY_NAME['x' + parts[0][1:]])
                elif parts[1].startswith(('w', 'x')):
                    # TODO: safe to assume reg value is constant?
                    if verbose: print '\tcmp_with (2) %r' % instruction.op_str
                    self.cmp_with = uc.reg_read(UC_REG_BY_NAME['x' + parts[1][1:]]) #int(parts[1][1:], 16)
                    self.cmp_delta = self.taint_offsets[int(parts[0][1:])]
                    self.cmp_ror = self.taint_rors[int(parts[0][1:])]
                    self.cmp_lhs = uc.reg_read(UC_REG_BY_NAME['x' + parts[0][1:]])

        if instruction.mnemonic in ('b.gt', 'b.le') and self.cmp_with is not None:
            if self.cmp_with - self.cmp_delta >= self.cmd_id:
                self.range_top = min(self.range_top, self.cmp_with - self.cmp_delta)
                if verbose: print '\trange top: %d' % self.range_top

        if instruction.mnemonic in ('b.eq', 'b.ne',) and self.cmp_with is not None:
            if self.cmp_with - self.cmp_delta > self.cmd_id:
                self.range_top = min(self.range_top, self.cmp_with - self.cmp_delta - 1)
                if verbose: print '\trange top: %d' % self.range_top

        if instruction.mnemonic in ('b.hi', 'b.ls') and self.cmp_with is not None:
            if self.cmp_delta < 0 and self.cmd_id < -self.cmp_delta:
                self.range_top = min(self.range_top, -self.cmp_delta - 1)
                if verbose: print '\trange top: %d' % self.range_top

            if self.cmp_ror != 0:
                if self.cmp_lhs > self.cmp_with:
                    same_count = ((1 << self.cmp_ror) - 1) - (self.cmp_lhs >> (32 - self.cmp_ror))
                    unrored = ((self.cmp_lhs >> (32 - self.cmp_ror)) | (self.cmp_lhs << self.cmp_ror)) & 0xFFFFffff
                    if verbose: print '\nunrored:', hex(unrored)
                    next_one = unrored + same_count + 1
                    if verbose: print '\nnext_one:', hex(next_one)
                    rerored = ((next_one << (32 - self.cmp_ror)) | (next_one >> self.cmp_ror)) & 0xFFFFffff
                    if verbose: print '\nrerored:', hex(rerored)
                    if rerored <= self.cmp_with:
                        self.range_top = min(self.range_top, self.cmd_id + same_count)
                else:
                    self.range_top = min(self.range_top, self.cmd_id)
                    self.switch_stride = 1 << self.cmp_ror

            if self.cmd_id + self.cmp_delta <= self.cmp_with and  self.cmp_ror == 0:
                self.range_top = min(self.range_top, self.cmp_with - self.cmp_delta)
                self.switch_top = self.cmp_with
                self.switch_stride = 1 << self.cmp_ror

                if verbose: print '\trange top: 0x%X' % self.range_top

        if instruction.mnemonic == 'ldrsw' and instruction.op_str.endswith(', lsl #2]') and int(parts[2][1:]) in self.taints and self.switch_stride == 1:
            switch_base = uc.reg_read(UC_REG_BY_NAME[parts[1]])
            current_index = uc.reg_read(UC_REG_BY_NAME[parts[2]])
            current = switch_base + self._simulator.sdword(switch_base + current_index * 4)
            same_count = 0
            for i in range(current_index + 1, self.switch_top + 1):
                if switch_base + self._simulator.sdword(switch_base + i * 4) != current:
                    break
                same_count += 1

            self.range_top = min(self.range_top, self.cmd_id + same_count)
            if verbose: print '\tswitchy (%d)' % self.range_top

            spoiled = int(parts[0][1:])
            if spoiled in self.taints:
                self.taints.remove(spoiled)
                del self.taint_offsets[spoiled]

        if instruction.mnemonic == 'and' and parts[0].startswith(('w', 'x')) and int(parts[0][1:]) in self.taints:
            spoiled = int(parts[0][1:])
            self.taints.remove(spoiled)
            del self.taint_offsets[spoiled]
            del self.taint_rors[spoiled]

        # TODO: is this sound?
        if instruction.mnemonic in ('ret', 'blr'):
            self.stopped = True
            if verbose: print 'stopping: range_top:', hex(self.range_top)
            return



class IPCServerTrace(object):
    def __init__(self, simulator, dispatch_func, cmd_id, buffer_size=0x1000, trace_branches=False):
        self.dispatch_func = dispatch_func
        self.cmd_id = cmd_id
        self._simulator = simulator
        self.description = None
        self.buffer_size = buffer_size

        #trace_branches = True
        if trace_branches:
            self.branch_tracer = BranchTracer(simulator, cmd_id)
            self._simulator.add_trace_instruction_hook(self.branch_tracer.trace_instruction)
        else:
            self.branch_tracer = None

    def is_correct(self):
        if self.description is None:
            return True
        if 'vt' not in self.description:
            return False
        # TODO: detect missing out-interfaces / in-interfaces
        return True

    def ret(self, uc, value):
        uc.reg_write(UC_ARM64_REG_X0, value)
        uc.reg_write(UC_ARM64_REG_PC, uc.reg_read(UC_ARM64_REG_LR))

    def PrepareForProcess(self, uc):
        arg = uc.reg_read(UC_ARM64_REG_X1)
        metainfo_size = 0x90
        metainfo_bytes = uc.mem_read(arg, metainfo_size)
        metainfo = list(struct.unpack('<' + 'I' * (metainfo_size/4), metainfo_bytes))

        self.bytes_in = metainfo[8/4] - 0x10
        assert 0 <= self.bytes_in <= 0x1000
        self.bytes_out = metainfo[0x10/4] - 0x10
        assert 0 <= self.bytes_out <= 0x1000
        self.buffer_count = metainfo[0x18/4]
        assert self.buffer_count < 20

        self.in_interface_count = metainfo[0x1c/4]
        self.out_interface_count = metainfo[0x20/4]
        self.in_handles_count = metainfo[0x24/4]
        self.out_handles_count = metainfo[0x28/4]

        assert self.in_interface_count < 20
        assert self.out_interface_count < 20
        assert self.in_handles_count < 20
        assert self.out_handles_count < 20
        
        self.description = {
            'inbytes': self.bytes_in,
            'outbytes': self.bytes_out,
            'ininterfaces': [None] * self.in_interface_count,
            'outinterfaces': [None] * self.out_interface_count,
            'inhandles': metainfo[0x4C/4:0x4C/4 + self.in_handles_count],
            'outhandles': metainfo[0x6C/4:0x6C/4 + self.out_handles_count],
            'buffers': metainfo[0x2c/4:0x2c/4 + self.buffer_count],
            'pid': metainfo[0] == 1,
        }
        self.description['lr'] = uc.reg_read(UC_ARM64_REG_LR)

        for i in ['outinterfaces', 'inhandles', 'outhandles', 'buffers', 'pid', 'ininterfaces']:
            if not self.description[i]:
                del self.description[i]

        if self.in_interface_count:
            self._simulator.add_trace_instruction_hook(self.trace_instruction)

        self.ret(uc, 0)
        return True

    def trace_instruction(self, uc, instruction):
        i = instruction
        #print '0x%08x:    %s  %s' % (instruction.address, instruction.mnemonic, instruction.op_str)
        if i.mnemonic == 'cmp' and i.op_str.endswith(', x9') and len(self.description['ininterfaces']) == 1 and self.description['ininterfaces'][0] is None:
            assert i.op_str == 'x8, x9' # oddly specific
            x9 = uc.reg_read(UC_ARM64_REG_X9)
            uc.reg_write(UC_ARM64_REG_X8, x9)
            uc.reg_write(UC_ARM64_REG_NZCV, 0b0100)
            self.description['ininterfaces'][0] = self._simulator.qword(x9)
        

    def OverwriteClientProcessId(self, uc):
        o = uc.reg_read(UC_ARM64_REG_X1)
        uc.mem_write(o, struct.pack('<Q', 0))
        #print' OverwriteClientProcessId', hex(struct.unpack('<Q', uc.mem_read(uc.reg_read(UC_ARM64_REG_X1), 8))[0])
        self.ret(uc, 0)
        return True

    def GetBuffers(self, uc):
        outptr = uc.reg_read(UC_ARM64_REG_X1)
        i = outptr
        while i < outptr + self.buffer_count * 0x10:
            uc.mem_write(i, struct.pack('<QQ', self._simulator.buffer_memory, self.buffer_size))
            i += 0x10
        uc.mem_write(self._simulator.buffer_memory, struct.pack('<Q', 1))
        self.ret(uc, 0)
        return True

    def GetInNativeHandles(self, uc):
        self.ret(uc, 0)
        return True

    def GetInObjects(self, uc):
        outptr = uc.reg_read(UC_ARM64_REG_X1)
        assert self.in_interface_count == 1
        uc.mem_write(outptr, struct.pack('<Q', self._simulator.in_object_ptr))
        self.ret(uc, 0)
        return True

    def BeginPreparingForReply(self, uc):
        o = uc.reg_read(UC_ARM64_REG_X1)
        uc.mem_write(o, struct.pack('<QQ', self._simulator.output_memory, 0x1000))
        self.ret(uc, 0)
        return True

    def SetBuffers(self, uc):
        self.ret(uc, 0)
        return True

    def SetOutObjects(self, uc):
        value = struct.unpack('<Q', uc.mem_read(uc.reg_read(UC_ARM64_REG_X1)+8, 8))[0]
        self.description['outinterfaces'][0] = self._simulator.qword(value)
        self.ret(uc, 0)
        return False

    def SetOutNativeHandles(self, uc):
        self.ret(uc, 0)
        return True

    def BeginPreparingForErrorReply(self, uc):
        return False

    def EndPreparingForReply(self, uc):
        self.ret(uc, 0)
        return False

    def target_function(self, offset, uc):
        if self.description is None:
            return False
        self.description['vt'] = offset
        self.ret(uc, 0)
        return True

my_cmd_ids = [0,     1, 2,    10,    11,    12,    13,    14,    15,    20,    21,    22,    23,    24,    25,    26,    27,    30,    31,    32,    33,    40,    50,    60,    65,    66,    67,    68,    70,    71,    80,    90,   100,   101,   102,   110,   111,   120,   121,   122,   123,   124,   500,  1000,  1001,]
def iter_traces(simulator, process_function):
    cmd_id = 0
    while True:
        trace = simulator.trace_cmd(process_function, cmd_id)
        if trace.description is not None:
            yield trace
            cmd_id += 1
        else:
            if trace.branch_tracer.range_top == 0xFFFFFFFF:
                break
            assert trace.branch_tracer.range_top >= cmd_id
            cmd_id = trace.branch_tracer.range_top + 1


def get_hashes(traces):
    prior_rets = {}
    hash_code_parts = []

    for trace in traces:
        description = trace.description
        # accumulate hash code
        suffix = ''
        if 'outinterfaces' in description:
            out_obj_name = description['outinterfaces'][0]
            if out_obj_name not in prior_rets:
                prior_rets[out_obj_name] = len(prior_rets)
            suffix = ';o%d' % prior_rets[out_obj_name]

        buffers = description.get('buffers', [])
        # didn't realize this was getting counted in the client code, but easier
        # to fix it here
        c_desc_size_extr = (buffers.count(10) + buffers.count(34))*2
        if buffers:
            suffix += ';b' + ','.join('%d' % i for i in buffers)
        suffix += ')'

        hash_code = '%d(%d%s' % (trace.cmd_id, (trace.bytes_in+3+c_desc_size_extr)/4, suffix)
        hash_code2 = '%d(%d%s' % (trace.cmd_id, (trace.bytes_in+3)/4, suffix)
        hash_code_parts.append((description.get('vt'), hash_code, hash_code2))

    hash_code_parts.sort()
    hash_code = ''.join(b for a,b,c in hash_code_parts)
    hash_code2 = ''.join(c for a,b,c in hash_code_parts)
    hashed = hashlib.sha224(hash_code).hexdigest()[:16]
    hashed2 = hashlib.sha224(hash_code2).hexdigest()[:16]

    return (hashed, hashed2, hash_code, hash_code2)

def find_hash_matches(hashed, hashed2):
    probably = None
    old_version = False
    if hashed in all_hashes:
        probably = all_hashes[hashed]
    elif hashed2 in all_hashes:
        probably = all_hashes[hashed2]
    elif hashed in all_hashes_300:
        old_version = True
        probably = all_hashes_300[hashed]
    elif hashed2 in all_hashes_300:
        old_version = True
        probably = all_hashes_300[hashed2]
    return probably, old_version





def find_s_table_symbols(f):
    stables = []
    for sym in f.symbols:
        if 's_Table' not in sym.name: continue
        address = DEFAULT_LOAD_BASE + sym.value
        stable_name = demangle(sym.name)
        # s_Table is removed by the demangler, but only if we're looking at a real IPC interface (ew)
        # 'nn::sf::hipc::detail::IHipcManager'
        if stable_name in ('nn::sf::cmif::server::CmifDomainServerObject',) or 's_Table' in stable_name:
            continue
        stables.append((sym.name, address))
        yield address, stable_name

def find_s_tables(f):
    candidates = []
    for offset, r_type, sym, addend in f.relocations:
        if addend:
            candidates.append((addend, offset))
    candidates.sort()

    f.binfile.seek(0)
    text_string = f.binfile.read(f.textsize)
    for regex in [
        # there's a unique error code (0x1A60A) used to find process functions
        # by matching the pattern:
        #   MOVK W?, #0xA60A
        '|'.join(re.escape(chr(0x40 | i) + '\xC1\x94\x72') for i in range(29)),

        # 5.x: match on the "SFCI" constant used in the template of s_Table
        #   MOV  W?, #0x4653
        #   MOVK W?, #0x4943, LSL#16
        '|'.join(re.escape(chr(0x60 | i) + '\xCA\x88\x52' + chr(0x60 | i) + '\x28\xA9\x72') for i in range(29)),

    ]:
        found = False
        for i in re.finditer(regex, text_string):
            if i.start() & 3: continue
            idx = bisect.bisect(candidates, (i.start(), 0))
            process_function, s_table = candidates[idx-1]
            if text_string.index('\xC0\x03\x5F\xD6', process_function) > i.start():
                yield DEFAULT_LOAD_BASE + s_table
                found = True
        if found:
            return

def trace_description_to_string(description, names):
    parts = []
    description = dict(description) # copy
    for k in ('outinterfaces', 'ininterfaces'):
        if k in description:
            description[k] = [(names.get(i, '0x%X' % (i,)) if i is not None else None) for i in description[k]]

    for i in ['vt', 'lr', 'inbytes', 'outbytes', 'buffers', 'inhandles', 'outhandles', 'outinterfaces', 'pid', 'ininterfaces']:
        if i not in description: continue
        if i in ('lr', 'vt'): continue
        v = description[i]
        if isinstance(v, (list, bool)):
            v = repr(v)
        else:
            if v >= 10:
                v = '0x%X' % v
            else:
                v = str(v)
            v = v.rjust(5)
        parts.append('"%s": %s' % (i, v))
    return '{%s}' % ', '.join(parts)




def description_to_string(process_name, interfaces, names):
    s = '%r: {\n' % (process_name,)
    for process_function, traces in sorted(interfaces.items()):
        s += '  %r: {\n' % names.get(process_function, '0x%X' % process_function)
        for cmd_id, desc in traces:
            s += '    %-8s%s,\n' % (str(cmd_id)+':', trace_description_to_string(desc, names))
        s += '  },\n'
    return s + '},'


def get_toplevel(data):
    not_toplevel = set()
    for i in data.values():
        for j in i.values():
            if 'outinterfaces' in j:
                for k in j['outinterfaces']:
                    not_toplevel.add(k)
    for i in not_toplevel:
        assert i in data
    #print not_toplevel
    return set(data.keys()) - not_toplevel

def simplify(a):
    a = dict(a)
    if "outinterfaces" in a:
        a['outinterfaces'] = True
    if "ininterfaces" in a:
        a['ininterfaces'] = True
    return a
def is_one_equal(a, b):
    return simplify(a) == simplify(b)

def compare(old, new):
    v = False
    score = 0
    removed_count = 0
    changed_count = 0
    same_count = 0
    added_count = 0
    for i in old.keys():
        if i not in new:
            #score -= 1
            if v: print 'removed:', i, old[i]
            removed_count += 1
        elif not is_one_equal(old[i], new[i]):
            if v: print 'changed:', i, old[i], new[i]
            changed_count += 1
        else:
            same_count += 1
    for i in new.keys():
        if i not in old:
            if v: print 'added:', i
            added_count += 1
    return same_count - removed_count

def dump_ipc_filename(fname):
    print '#', fname
    #if fname.endswith(('.id0', '.id1', '.nam'))
    with open(fname, 'rb') as fileobj:
        #if fileobj.read(4) not in ('NSO0', 'KIP1'):
        #    return
        fileobj.seek(0)
        f = nxo64.load_nxo(fileobj)

    simulator = IPCServerSimulator(f)

    s_tables = {v: simulator.qword(v) for v in find_s_tables(f)}


    interfaces = {}
    hash_codes = {}
    for process_function in s_tables.values():
        traces = list(iter_traces(simulator, process_function))
        hashed, hashed2, hash_code, hash_code2 = get_hashes(traces)
        hash_codes[process_function] = (hashed, hashed2)
        interfaces[process_function] = [(t.cmd_id, t.description) for t in traces]

    if not interfaces: return

    names = {s_tables[a]: b for a,b in find_s_table_symbols(f)}

    process_name = fname.split('/')[-1]
    if process_name == 'ldr': process_name = 'loader'
    new_data = eval('{%s}' % description_to_string(process_name, interfaces, names))[process_name]

    needs_names = all(i.startswith('0x') for i in new_data)

    if needs_names:
        if process_name in reference_data:
            old_data = reference_data[process_name]
            names_to_apply = []
            for name in old_data:
                matches = sorted((compare(old_data[name], new_data[k]), k) for k in new_data)
                if matches[-1][0] > 0 and matches[-1][0] > matches[-2][0] + 1:
                    names_to_apply.append((matches[-1][0]-matches[-2][0], name, matches[-1][1]))

            names_to_apply.sort(reverse=True)
            for i in names_to_apply:
                names[int(i[2],16)] = i[1]
                new = new_data[i[2]]
                old = old_data[i[1]]
                for cmd in new.keys():
                    if cmd in old and "outinterfaces" in new[cmd] and is_one_equal(old[cmd], new[cmd]):
                        names[int(new[cmd]['outinterfaces'][0],16)] = old[cmd]['outinterfaces'][0]

        for i in new_data.keys():
            if int(i,16) not in names:
                probably, old_version = find_hash_matches(*hash_codes[int(i, 16)])
                if probably:
                    if not old_version and len(probably) == 1:
                        names[int(i, 16)] = probably[0]
                    else:
                        print '# hash: ',i,probably

    print description_to_string(process_name, interfaces, names)

    #print get_toplevel(old_data)
    #print get_toplevel(new_data)

    return
    s_tables = []
    process_functions = []
    process_function_names = {}


    old_data = reference_data.get(process_name, {})
    #old_top_level_names = old_data.keys()

    all_traces = []
    names = {}
    messages = {}
    for process_function in process_functions:
        #if process_function != 0x7100003074: continue

        traces = iter_traces(simulator, process_function)
        traces = list(traces)

        msg = None
        if process_function in process_function_names:
            name = process_function_names[process_function]
        else:
            # try to figure out name for 4.0+
            hashed, hashed2, hash_code, hash_code2 = get_hashes(traces)
            probably, old_version = find_hash_matches(hashed, hashed2)

            if probably is not None:
                probably_in_module = [i for i in probably if i in old_data]
                if len(probably_in_module) == 1 and not old_version:
                    names[process_function] = probably_in_module[0]
                    #if old_version:
                     #   msg = 'single hash match (in module) %r' % (probably_in_module[0],)
                elif len(probably) == 1:
                    # TODO: need to figure this out earlier
                    #name = probably[0]
                    msg = 'single hash match %r' % (probably[0],)
                    #names[process_function] = probably[0]
                else:
                    msg = repr(probably)
                if old_version:
                    msg = '3.0.0: ' + msg
            else:
                msg = '%s %r' % (hashed, hash_code)
                if hash_code != hash_code2:
                    msg += ' %r' % (hash_code2,)
            if messages is not None:
                messages[process_function] = msg
        all_traces.append((process_function, traces))


    for process_function, traces in all_traces:
        if process_function not in names:
            continue
        name = names[process_function]
        if name not in old_data:
            continue
        old_traces = old_data[name]
        for trace in traces:
            if trace.cmd_id not in old_traces:
                continue
            old_trace = old_traces[trace.cmd_id]
            description = trace.description
            if 'outinterfaces' not in description:
                continue

            if len(description['outinterfaces']) != 1:
                continue
            if len(old_trace['outinterfaces']) != 1:
                continue
            func = simulator.qword(description['outinterfaces'][0])
            if func in names:
                continue
            names[func] = old_trace['outinterfaces'][0]

            #print old_trace
            #print '', trace.description

    print '%r: {' % (process_name,), '#', fname
    #assert len(set(names.values())) == len(names)
    for process_function, traces in all_traces:
        name = names.get(process_function, '0x%X' % process_function)
        msg = messages.get(process_function)
        if msg is None:
            print '  ' + repr(name) + ': {'
        else:
            print '  ' + repr(name) + ': { #', msg
        for trace in traces:
            description = trace.description
            line = '      ' + ('%d: ' % trace.cmd_id).ljust(7) + '{'
            parts = []
            for k in ('outinterfaces', 'ininterfaces'):
                if k in description:
                    description[k] = [(names.get(simulator.qword(i), '0x%X' % (simulator.qword(i),)) if i is not None else None) for i in description[k]]

            for i in ['vt', 'lr', 'inbytes', 'outbytes', 'buffers', 'inhandles', 'outhandles', 'outinterfaces', 'pid', 'ininterfaces']:
                if i not in description: continue
                #if PUBLIC and i in ('vt', 'lr'): continue
                if i in ('lr', 'vt'): continue
                v = description[i]
                if isinstance(v, (list, bool)):
                    v = repr(v)
                else:
                    if v >= 10:
                        v = '0x%X' % v
                    else:
                        v = str(v)
                    v = v.rjust(5)
                parts.append('"%s": %s' % (i, v))
            line += ', '.join(parts)

            line += '},'
            print line

        print '  },'
        #if PUBLIC:
        #   print '  },'
        #else:
        #   print '  }, # ' + msg

    print '},'

    unmatched_names = set(old_data.keys()) - set(names.values())
    print '# unmatched_names:', sorted(unmatched_names)
def main(fnames):
    for i in fnames:
        dump_ipc_filename(i)

if __name__ == '__main__':
    main(sys.argv[1:])

