import sys
import struct

from unicorn import *
from unicorn.arm64_const import *
from capstone import *

import nxo64
from ipcclient import iter_vtables_in_nxo, demangle

from unicornhelpers import load_nxo_to_unicorn, create_unicorn_arm64

class Simulator(object):
    def __init__(self, f, verbose=False):
        self.verbose = verbose
        self.uc = uc = create_unicorn_arm64()
        uc.hook_add(UC_HOOK_CODE, self.hook_code)

        self.loadbase = 0x7100000000
        self.return_magic = 0xAA00000000
        uc.mem_map(self.return_magic, 0x1000)
        load_nxo_to_unicorn(uc, f, self.loadbase)

        stack = 0x100000000
        stack_size = 0x2000
        uc.mem_map(stack, stack_size)
        self.stack_top = stack
        self.stack_base = stack + stack_size

        self.mem = mem = 0x200000000
        mem_size = 0x5000
        uc.mem_map(mem, mem_size)

        self.tls = 0x300000000
        tls_size = 0x1000
        uc.mem_map(self.tls, tls_size)
        uc.mem_write(self.tls + 0x1f8, struct.pack('<Q', self.tls))

        self.heap = heap = 0x400000000
        self.heap_size = heap_size = 0x4000
        uc.mem_map(heap, heap_size)
        self.heap_ptr = heap

        self.stack_args = 6
        self.arg_scratch = 0x10000000
        self.arg_scratch_size = (9+self.stack_args) * 0x1000
        uc.mem_map(self.arg_scratch, self.arg_scratch_size)

        hax_code_ptr = 0x500000000
        hax_code_size = 0x1000
        uc.mem_map(hax_code_ptr, hax_code_size)
        uc.mem_write(hax_code_ptr, struct.pack('<II', 0xd65f03c0, 0xd65f03c0)) #0xd65f03c0))

        self.ret_instruction_ptr = hax_code_ptr # self.loadbase + 0x15C
        self.alloc_instruction_ptr = hax_code_ptr + 4 # self.loadbase + 0x15C

        uc.mem_write(mem, ''.join(struct.pack('<I', 0x41000000 + (i<<16)) for i in range(64)))
        uc.mem_write(mem + 0x1000, ''.join(struct.pack('<I', 0x42000000 + (i<<16)) for i in range(64)))
        uc.mem_write(mem + 0x2000, ''.join(struct.pack('<I', 0x43000000 + (i<<16)) for i in range(64)))
        uc.mem_write(mem + 0x3000, ''.join(struct.pack('<I', 0x44000000 + (i<<16)) for i in range(64)))
        uc.mem_write(mem + 0x4000, ''.join(struct.pack('<I', 0x45000000 + (i<<16)) for i in range(64)))

        uc.mem_write(mem + 8, struct.pack('<Q', 0x0101010101010101))
        uc.mem_write(mem + 0x10, struct.pack('<Q', mem + 0x1000))
        uc.mem_write(mem + 0x1000, struct.pack('<Q', mem + 0x2000))
        uc.mem_write(mem + 0x2000, struct.pack('<Q', self.ret_instruction_ptr))
        uc.mem_write(mem + 0x2008, struct.pack('<Q', self.ret_instruction_ptr))
        uc.mem_write(mem + 0x2010, struct.pack('<Q', self.ret_instruction_ptr))

        uc.mem_write(mem + 0x20, struct.pack('<Q', mem + 0x3000))
        uc.mem_write(mem + 0x30, struct.pack('<Q', mem + 0x3000))
        uc.mem_write(mem + 0x3000, struct.pack('<Q', mem + 0x4000))
        uc.mem_write(mem + 0x4000 + 0x10, struct.pack('<Q', self.alloc_instruction_ptr))

        self.malloc_funcs = {
            self.alloc_instruction_ptr: UC_ARM64_REG_X1,
        }
        # free funcs and mutex lock/unlock
        self.skip_funcs = []

        self.current_run = None

        if False:
            uc.hook_add(UC_HOOK_MEM_READ, self.hook_mem_read)
            uc.hook_add(UC_HOOK_MEM_WRITE, self.hook_mem_write)

    def hook_mem_read(self, uc, e, addr, sz, *args):
        #print 'hook_mem_read:', hex(addr), sz
        if self.arg_scratch <= addr < self.arg_scratch + self.arg_scratch_size:
            print 'read from arg:', ((addr - self.arg_scratch) / 0x1000) + 1, '@ + 0x%X-0x%X' % (addr & 0xFFF, (addr & 0xFFF) + sz)

    def hook_mem_write(self, uc, e, addr, sz, *args):
        #print 'hook_mem_read:', hex(addr), sz
        if self.arg_scratch <= addr < self.arg_scratch + self.arg_scratch_size:
            print 'write to arg:', ((addr - self.arg_scratch) / 0x1000) + 1, '@ + 0x%X-0x%X' % (addr & 0xFFF, (addr & 0xFFF) + sz)


    def dump_regs(self, uc):
        values = []
        for i in range(28):
            values.append(('X%d' % i, uc.reg_read(UC_ARM64_REG_X0+i)))
        values.append(('X29', uc.reg_read(UC_ARM64_REG_X29)))
        values.append(('X30', uc.reg_read(UC_ARM64_REG_X30)))
        values.append(('SP', uc.reg_read(UC_ARM64_REG_SP)))
        values.append(('PC', uc.reg_read(UC_ARM64_REG_PC)))
        print '', ', '.join('%s=%X' % i for i in values)

    def dump_state(self, uc, pc):
        md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
        i = md.disasm(str(uc.mem_read(pc, 4)), pc).next()
        print " " + "_" * 80
        print " instruction @ 0x%X: %7s %s" % (pc, i.mnemonic, i.op_str)
        self.dump_regs(uc)

    def hook_code(self, uc, address, size, user_data):
        if address == self.return_magic:
            uc.emu_stop()
            return
        if self.verbose:
            self.dump_state(uc, address)
        instr = struct.unpack('<I', uc.mem_read(address, 4))[0]


        if 0xD53BD060 <= instr <= 0xd53bd07e: # mov x?, tls
            uc.reg_write(UC_ARM64_REG_X0 + (instr-0xD53BD060), self.tls)
            uc.reg_write(UC_ARM64_REG_PC, address+4)
        if instr == 0xd4000421: # svc 0x22
            if self.current_run is not None:
               self.current_run.ipcbuf = self.read(self.tls, 0x100)
            uc.emu_stop()
            return
            #uc.reg_write(UC_ARM64_REG_X0, 0)
            #uc.reg_write(UC_ARM64_REG_PC, address+4)
        if instr & (0b111111 << 26) == (0b100101 << 26):
            self.check_bl_for_malloc(uc)
            self.check_bl_for_WriteBufferDataImpl(uc)
            self.check_bl_for_bad_mutex(uc)
            

        if address in self.malloc_funcs:
            size_reg = self.malloc_funcs[address]
            size = uc.reg_read(size_reg)
            out = self.heap_ptr
            self.heap_ptr += (size + 0xF) & ~0xF
            #print ' malloc hook (0x%X) -> 0x%X' % (size, out)
            uc.reg_write(UC_ARM64_REG_X0, out)
            uc.reg_write(UC_ARM64_REG_PC, uc.reg_read(UC_ARM64_REG_X30))
        if address in self.skip_funcs:
            uc.reg_write(UC_ARM64_REG_PC, uc.reg_read(UC_ARM64_REG_X30))

    def check_bl_for_bad_mutex(self, uc):
        if uc.reg_read(UC_ARM64_REG_X0) == 0x200003008:
            #print 'SKIPPING MUTEX'
            uc.reg_write(UC_ARM64_REG_PC, uc.reg_read(UC_ARM64_REG_PC) + 4)


    def check_bl_for_malloc(self, uc):
        self.bl_count += 1
        if self.verbose:
            print 'BL COUNT ', self.bl_count, uc.reg_read(UC_ARM64_REG_X0), uc.reg_read(UC_ARM64_REG_X1)
        if self.bl_count == 2 and uc.reg_read(UC_ARM64_REG_X0) in (0x20, 0x30, 0x38):
            #print 'MATCHED MALLOC'
            size = uc.reg_read(UC_ARM64_REG_X0)
            out = self.heap_ptr
            self.heap_ptr += (size + 0xF) & ~0xF
            uc.reg_write(UC_ARM64_REG_X0, out)
            uc.reg_write(UC_ARM64_REG_PC, uc.reg_read(UC_ARM64_REG_PC) + 4)
        elif self.bl_count == 4 and uc.reg_read(UC_ARM64_REG_X1) in (0x20, 0x30, 0x38) and uc.reg_read(UC_ARM64_REG_X0) in (0, 0x200004000):
            #print 'MATCHED AllocateFromExpHeap'
            size = uc.reg_read(UC_ARM64_REG_X1)
            out = self.heap_ptr
            self.heap_ptr += (size + 0xF) & ~0xF
            uc.reg_write(UC_ARM64_REG_X0, out)
            uc.reg_write(UC_ARM64_REG_PC, uc.reg_read(UC_ARM64_REG_PC) + 4)


    def check_bl_for_WriteBufferDataImpl(self, uc):
        #  nn::sf::hipc::client::Hipc2ClientCoreProcessorImpl::WriteBufferDataImpl
        # nn::sf::hipc::detail::HipcMessageWriter *
        arg0 = uc.reg_read(UC_ARM64_REG_X0)
        if arg0 < self.stack_top or arg0 > self.stack_base:
            return
        # int
        arg1 = uc.reg_read(UC_ARM64_REG_X1) & 0xFFFFFFFF
        if arg1 == 0 or arg1 > 32:
            return
        # nn::sf::detail::PointerAndSize const*
        arg2 = uc.reg_read(UC_ARM64_REG_X2)
        if arg2 < self.stack_top or arg2 > self.stack_base:
            return
        # int const*
        arg3 = uc.reg_read(UC_ARM64_REG_X3)
        if arg3 < self.stack_top or arg3 > self.stack_base:
            return
        # unsigned long
        arg4 = uc.reg_read(UC_ARM64_REG_X4)
        if arg4 > 0xFFFF:
            return
        # unsigned long
        arg5 = uc.reg_read(UC_ARM64_REG_X5)
        if arg5 > 0x1000:
            return

        if self.current_run is not None:
            self.current_run.buffers = [self.dword(arg3 + i*4) for i in xrange(arg1)]

        uc.reg_write(UC_ARM64_REG_X4, 0xF000)


    def _do_call(self, func, arg0):
        self.heap_ptr = self.heap
        self.bl_count = 0
        self.uc.mem_write(self.heap, '\0' * self.heap_size)
        self.uc.mem_write(self.arg_scratch, '\0' * self.arg_scratch_size)
        self.uc.mem_write(self.tls, '\0' * 0x100)

        self.uc.reg_write(UC_ARM64_REG_SP, self.stack_base-(self.stack_args*8))
        self.uc.reg_write(UC_ARM64_REG_X0, arg0)
        self.uc.reg_write(UC_ARM64_REG_X30, self.return_magic)

        for i in range(1, 9+self.stack_args):
            arg = self.arg_scratch + (i-1) * 0x1000
            self.uc.mem_write(arg, struct.pack('<Q', arg + 0x800))
            self.uc.mem_write(arg + 0x800, struct.pack('<Q', self.mem + 0x2000))
            if i < 9:
                self.uc.reg_write(UC_ARM64_REG_X0+i, arg)
            else:
                i -= 9
                ap = self.stack_base-(self.stack_args*8) + i*8
                self.uc.mem_write(ap, struct.pack('<Q', arg))

        try:
            self.uc.emu_start(self.loadbase + func, 0)
        except UcError as e:
            print 'TODO: UcError (around 0x%X): %s' %  (self.uc.reg_read(UC_ARM64_REG_PC), e)

    def call(self, func, arg0):
        assert self.current_run is None
        run = RunData()
        self.current_run = run
        self._do_call(func, arg0)
        self.current_run = None
        return run

    def read(self, addr, size):
        return self.uc.mem_read(addr, size).decode('latin-1').encode('latin-1')

    def qword(self, addr):
        return struct.unpack('<Q', self.uc.mem_read(addr, 8))[0]
    def dword(self, addr):
        return struct.unpack('<I', self.uc.mem_read(addr, 4))[0]

class RunData(object):
    def __init__(self):
        self.buffers = []
        self.ipcbuf = None

def pretty_hex(v):
    assert v >= 0
    if v < 10:
        return '%d' % v
    return '0x%X' % v

all_hashes = {}

import hashlib
def sim_filename(fname):
    with open(fname, 'rb') as fileobj:
        f = nxo64.load_nxo(fileobj)

    if 0:
        sim = Simulator(f, True)
    else:
        sim = Simulator(f, False)

    for vtable in iter_vtables_in_nxo(f):
        ## blacklist some things which abort because idk what to do atm
        #if 'nn::am::service::IApplicationAccessor' in vtable.interface: continue
        #if 'nn::am::service::IAppletAccessor' in vtable.interface: continue
        #if 'nn::am::service::ILibraryAppletAccessor' in vtable.interface: continue

        if 'IUnknown_' in vtable.interface:
            continue # skip anything we can't name

        display = False # 'IUnknown_' in vtable.interface
        if display:
            print
            print vtable.interface
            print '=' * len(vtable.interface)
        else:
            pass
            print vtable.interface
        
        hash_code = ''
        prior_rets = {}
        for entry in vtable.entries:
            #print '%r (%x)' % (entry.cmd, 0x7100000000+ entry.funcptr)
            if entry.cmd is None: continue

            run_data = sim.call(entry.funcptr, sim.mem)
            ipcbuf = run_data.ipcbuf
            buffers = run_data.buffers

            if False:
                for addr in range(sim.arg_scratch, sim.arg_scratch + sim.arg_scratch_size - 0x1000, 0x1000):
                    val = sim.qword(addr)
                    if val != addr + 0x800:
                        print 'value in arg', ((addr - sim.arg_scratch) / 0x1000) + 1, hex(val)

            parts = []


            if buffers:
                parts.append('buffers types ' + ', '.join(map(pretty_hex, buffers)))

            if ipcbuf is None:
                continue
            assert ipcbuf is not None
            assert ipcbuf.count('SFCI') == 1

            w0, w1 = struct.unpack_from('<II', ipcbuf, 0)
            #print hex(w0)
            assert (w0 & 0xFFFF) in (4, 6)
            x_count = (w0 >> 16) & 0xF
            a_count = (w0 >> 20) & 0xF
            b_count = (w0 >> 24) & 0xF
            w_count = (w0 >> 28)
            assert not w_count

            inline_data_length = (w1 & 0x3FF) * 4
            aligned_data_length = inline_data_length - 0x10
            has_handle_desc = (w1 >> 31) == 1
            header_words = 2
            if has_handle_desc:
                w2 = struct.unpack_from('<I', ipcbuf, header_words * 4)[0]
                header_words += 1

                has_pid = (w2 & 1) == 1
                copy_count = (w2 >> 1) & 0xf
                move_count = (w2 >> 5) & 0xf
                if has_pid:
                    header_words += 2
                    parts.append('send pid')
                    #print ' has pid'
                if copy_count: parts.append('%d copied handles in' % copy_count)
                if move_count: parts.append('%d moved handles in' % move_count) # print ' move_count', move_count
                header_words += copy_count + move_count

            header_words += x_count * 2 + a_count * 3 + b_count * 3

            while header_words & 3:
                header_words += 1

            data = ipcbuf[header_words*4:header_words*4+aligned_data_length]
            assert data[0:4] == 'SFCI' or data[0x10:0x14] == 'SFCI'
            if data[0x10:0x14] == 'SFCI':
                in_objects = struct.unpack_from('B', data, 1)[0]
                if in_objects:
                    parts.append('%d in objects' % in_objects)
                    #print ' in_objects:', in_objects
                in_size_exact = struct.unpack_from('H', data, 2)[0]
                in_size = in_size_exact - 0x10
                parts.append('%s bytes in' % pretty_hex(in_size))
            else:
                in_size = len(data) - 0x10
                if len(data) == 0x10:
                    parts.append('0 bytes in')
                else:
                    parts.append('~%s bytes in' % pretty_hex(in_size))

            if entry.cmd != struct.unpack_from('<Q', data, data.index('SFCI') + 8)[0]:
                print 'bad', entry.cmd, struct.unpack_from('<Q', data, data.index('SFCI') + 8)[0], hex(entry.funcptr)
                entry.cmd = struct.unpack_from('<Q', data, data.index('SFCI') + 8)[0]

            out_obj = struct.unpack('<Q', sim.uc.mem_read(sim.heap, 8))[0]
            if not out_obj:
                assert sim.heap_ptr == sim.heap
            suffix = ''
            if out_obj:
                rtti = sim.qword(out_obj-8)
                if rtti > sim.loadbase:
                    name = sim.read(sim.qword(rtti+8), 512)
                    while '\0' not in name:
                        name += sim.read(sim.qword(rtti+8) + len(name), 512)
                    name = name[:name.index('\0')]

                    out_obj_name = demangle(name)
                elif out_obj - sim.loadbase - 16 in f.addr_to_name:
                    out_obj_name = demangle(f.addr_to_name[out_obj - sim.loadbase - 16])
                else:
                    out_obj_name = 'unk_0x%X' % out_obj
                if out_obj_name not in prior_rets:
                    prior_rets[out_obj_name] = len(prior_rets)
                suffix = ';o%d' % prior_rets[out_obj_name]
                
                parts.append('returns interface %s' % out_obj_name)

            row =  '0x%X || %5d || ' % (0x7100000000 + entry.funcptr, entry.cmd,) # sim.loadbase + entry.funcptr)

            if entry.funcptr in f.addr_to_name:
                row += demangle(f.addr_to_name[entry.funcptr]).split('>::_nn_sf_sync_')[-1].split('(')[0].ljust(len('ProxyProcedureToAcquireApplicationAuthorizationForNintendoAccount'))
            row += ' || '

            if display:
                print row + ' - '.join(parts) + ' ||'

            hash_code += '%d(%d%s' % (entry.cmd, (in_size+3)/4, suffix)
            if buffers:
                hash_code += ';b' + ','.join('%d' % i for i in buffers)
            hash_code += ')'

        if True:        

            hashed = hashlib.sha224(hash_code).hexdigest()[:16]

            #print hashed, repr(hash_code)
            if 'IUnknown_' not in vtable.interface:
                if vtable.interface not in all_hashes.get(hashed, []):
                    all_hashes.setdefault(hashed, []).append(vtable.interface)
    #print all_hashes

def main():
    for i in sys.argv[1:]:
        print 'doing %r...' % (i,)
        sim_filename(i)
    with open('hashes_gen.py', 'w') as f:
        f.write('all_hashes = %r\n' % all_hashes)

if __name__ == '__main__':
    main()

