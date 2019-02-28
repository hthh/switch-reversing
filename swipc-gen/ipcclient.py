import struct
from collections import Counter
import hashlib
import re

from capstone import *
from capstone.arm64 import *

from nxo64 import load_nxo
from demangling import get_demangled
IDA_BASE = 0x7100000000

MANUAL_NAME_LOOKUP = {
	# 4.0.1 loader:
	"IUnknown_b171b62c_0x7100051A28": "nn::lr::ILocationResolverManager",
	"IUnknown_bd070344_0x7100051A98": "nn::lr::ILocationResolver",
	"IUnknown_788b7338_0x7100051B38": "nn::lr::IRegisteredLocationResolver",
	"IUnknown_0868914f_0x7100051BC8": "nn::lr::IAddOnContentLocationResolver",

	# 4.0.1 fs:
	"IUnknown_b171b62c_0x71001CC688": "nn::lr::ILocationResolverManager",
	"IUnknown_bd070344_0x71001CC6F8": "nn::lr::ILocationResolver",
	"IUnknown_788b7338_0x71001CC798": "nn::lr::IRegisteredLocationResolver",
	"IUnknown_0868914f_0x71001CC828": "nn::lr::IAddOnContentLocationResolver",
	"IUnknown_dfd5f913_0x71001CC890": "nn::psc::sf::IPmService",
	"IUnknown_b171b62c_0x71001CC8E8": "nn::psc::sf::IPmModule",
	"IUnknown_0b7cc0c3_0x71001CC4E0": "nn::tma::IFileManager",
	"IUnknown_9329709d_0x71001CC590": "nn::tma::IFile",
	"IUnknown_b171b62c_0x71001CC618": "nn::tma::IDirectory",
	"IUnknown_dfd5f913_0x71001CC378": "nn::pinmux::IManager",
	"IUnknown_0868914f_0x71001CC3D0": "nn::pinmux::ISession",

	# 4.0.1 pm:
	"IUnknown_b171b62c_0x710004B8F8": "nn::ldr::detail::IProcessManagerInterface",

	# 4.0.1 nvservices:
	"IUnknown_dfd5f913_0x710011A940": "nn::psc::sf::IPmService",
	"IUnknown_dfd5f913_0x710011A998": "nn::psc::sf::IPmModule",

	# 4.0.1 ns:
	"IUnknown_560d510c_0x7100191930": "nn::nim::detail::INetworkInstallManager",
	"IUnknown_0868914f_0x7100191C18": "nn::nim::detail::IAsyncResult",
	"IUnknown_b171b62c_0x7100191C80": "nn::nim::detail::IAsyncValue",
	"IUnknown_ef63a7f7_0x7100191CF0": "nn::nim::detail::IAsyncData",
	"IUnknown_a2ec7c94_0x7100189400": "nn::es::IETicketService",
	"IUnknown_f4e4f171_0x710018A7E0": "nn::ldr::detail::IShellInterface",
	"IUnknown_b171b62c_0x710018A840": "nn::lr::ILocationResolverManager",
	"IUnknown_bd070344_0x710018A8B0": "nn::lr::ILocationResolver",
	"IUnknown_788b7338_0x710018A950": "nn::lr::IRegisteredLocationResolver",
	"IUnknown_0868914f_0x710018A9E0": "nn::lr::IAddOnContentLocationResolver",
	"IUnknown_f4e4f171_0x710018F1B0": "nn::pm::detail::IBootModeInterface",
	"IUnknown_bd070344_0x710018F210": "nn::pm::detail::IShellInterface",
	"IUnknown_5c4120bd_0x7100195E60": "nn::pdm::detail::INotifyService",

	# 4.0.1 fatal:
	"IUnknown_0ee18a67_0x7100159718": "nn::spsm::detail::IPowerStateInterface",
	"IUnknown_dfd5f913_0x710015DCA8": "nn::pm::detail::IInformationInterface",


	# 4.0.1 friends:
	'IUnknown_271cf7f3_0x71001C4390': 'nn::pdm::detail::IQueryService',


	# 3.0.0 fs:
	#"IUnknown_0b7cc0c3_0x71001C2640": "nn::tma::IFileManager",



}

MANUAL_NAME_LOOKUP = {
	

}


def demangle(s):
	value = get_demangled(s)
	if '<nn::sf::cmif::client::CmifProxyFactory<' in value:
		value = value.split('<nn::sf::cmif::client::CmifProxyFactory<')[1].split(', ')[0]
	elif '<nn::sf::cmif::client::detail::CmifProxy<' in  value:
		value = value.split('<nn::sf::cmif::client::detail::CmifProxy<')[1].split(', ')[0]

	if 'nn::sf::UnmanagedServiceObject<' in value:
		value = value.split('nn::sf::UnmanagedServiceObject<')[1].split(', ')[0]

	return value

def find_ret(binstring, func_start):
	offset = func_start
	while struct.unpack_from('<I', binstring, offset)[0] != 0xd65f03c0:
		offset += 4
	return offset

lookup = {}

def get_last_immediate_argument(insns):
	immregs = [None] * 32

	stores = {}
	for i in insns:
		if i.mnemonic == 'orr' and i.op_str.split(', ')[1] == 'wzr':
			immregs[int(i.op_str.split(', ')[0][1:])] = i.operands[2].value.imm
		elif i.mnemonic == 'mov':
			src = i.op_str.split(', ')[1]
			dest = int(i.op_str.split(', ')[0][1:])
			if src == 'wzr' or src == 'xzr':
				immregs[dest] = 0
			elif src == 'sp':
				immregs[dest] = None
			else:
				immregs[dest] = immregs[int(src[1:])]
		elif i.mnemonic == 'movz':
			if i.op_str.endswith(', lsl #16'):
				immregs[int(i.op_str.split(', ')[0][1:])] = i.operands[1].value.imm << 16
			else:
				immregs[int(i.op_str.split(', ')[0][1:])] = i.operands[1].value.imm
		elif i.mnemonic == 'movk':
			immregs[int(i.op_str.split(', ')[0][1:])] |= i.operands[1].value.imm
		elif i.mnemonic == 'str' and i.reg_name(i.operands[1].value.mem.base) == 'sp':
			reg = i.reg_name(i.operands[0].value.mem.base)
			if reg == 'wzr':
				value = 0
			else:
				value = immregs[int(reg[1:])]
			stores[i.operands[1].value.mem.disp] = value
		elif i.mnemonic == 'stp' and i.reg_name(i.operands[2].value.mem.base) == 'sp':
			reg = i.reg_name(i.operands[0].value.mem.base)
			if reg == 'wzr':
				value = 0
			else:
				value = immregs[int(reg[1:])]
			stores[i.operands[2].value.mem.disp] = value

			reg = i.reg_name(i.operands[1].value.mem.base)
			if reg == 'wzr':
				value = 0
			else:
				value = immregs[int(reg[1:])]
			stores[i.operands[2].value.mem.disp + 8] = value

	if stores:
		last_store = None
		end = sorted(stores.keys())[-1] + 8
		for off in range(0, end, 8):
			if off not in stores:
				break
			val = stores[off]
			if val is not None:
				last_store = val
		if last_store is not None:
			return last_store

	for i in range(8, -1, -1):
		if immregs[i] is not None:
			return immregs[i]

	return None



is_process_function_cache = {}
def is_process_function(binstring, func_start):
	#print hex(func_start)
	if func_start in is_process_function_cache:
		return is_process_function_cache[func_start]
	md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
	counter = 0
	try:
		i = func_start
		instr = md.disasm(binstring[i:i+4], i).next()
		while instr.mnemonic not in ('ret',):
			#if instr.mnemonic in ('movz', 'movk'):
			#	print instr.mnemonic, repr(instr.op_str), instr.op_str.endswith(', #0x4653')
			#print instr.mnemonic
			if instr.mnemonic in ('movz', 'movk') and instr.op_str.endswith(', #0x4943, lsl #16'):
				counter += 1
				#print '...'
			elif instr.mnemonic in ('movz', 'movk') and instr.op_str.endswith(', #0x4f43, lsl #16'):
				#print '..'
				counter += 1
			elif instr.mnemonic in ('movz', 'movk') and instr.op_str.endswith(', #0x4653'):
				#print '.'
				counter += 1
			i += 4
			instr = md.disasm(binstring[i:i+4], i).next()
		func_end = i + 4
	except StopIteration:
		is_process_function_cache[func_start] = False
		return False
	#print counter
	is_process_function_cache[func_start] = (counter in (2,4))
	return (counter in (2,4))

def get_function_cmd_id_old(binstring, func_start, func_end, rostart, roend):
	md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
	counter = 0
	got_movz = False
	got_movk = False
	for i in range(func_start, func_end, 4):
		try:
			instr = md.disasm(binstring[i:i+4], i).next()
		except StopIteration:
			return None
		if instr.mnemonic == 'movz' and instr.op_str.endswith(', #0x4f43, lsl #16'):
			got_movz = True
		elif instr.mnemonic == 'movk' and instr.op_str.endswith(', #0x4653'):
			got_movk = True
		if got_movk and got_movz:
			break

	if not got_movz and got_movk:
		return None


	md.detail = True
	constants = {}
	for i in range(func_start, func_end, 4):
		try:
			instr = md.disasm(binstring[i:i+4], i).next()
		except StopIteration:
			return None

		if instr.mnemonic == 'adrp':
			reg_name = instr.reg_name(instr.operands[0].value.reg)
			constants[reg_name] = instr.operands[1].value.imm
		elif instr.mnemonic == 'add' and instr.operands[2].type == ARM64_OP_IMM:
			reg_name = instr.reg_name(instr.operands[1].value.reg)
			if reg_name in constants:
				loc = instr.operands[2].value.imm + constants[reg_name]
				if rostart <= loc <= roend-0x10:
					if binstring[loc:loc+8] == 'SFCI\0\0\0\0':
						return struct.unpack_from('<Q', binstring, loc + 8)[0]
				if instr.reg_name(instr.operands[1].value.reg) == reg_name:
					del constants[reg_name]
		elif instr.mnemonic in ('bl', 'blr'):
			constants = {}

	return None

def get_function_cmd_id(binstring, func_start, plt_lookup, rostart, roend):
	md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
	md.detail = True

	func_end = find_ret(binstring, func_start) + 4
	#print 'func_end: 0x%X' % func_end
	calls = 0
	block_starts = set()
	block_starts.add(func_start)
	for i in range(func_start, func_end, 4):
		try:
			insn = md.disasm(binstring[i:i+4], i).next()
		except StopIteration:
			break
		if insn.mnemonic in ('bl', 'blr'):
			calls += 1
			block_starts.add(i+4)
		elif insn.mnemonic == 'cbz':
			block_starts.add(i+4)
			block_starts.add(insn.operands[1].value.imm)

	if calls >= 4:
		cmd_id_old = get_function_cmd_id_old(binstring, func_start, func_end, rostart, roend)
		if cmd_id_old is not None:
			return cmd_id_old, None

	#print block_starts
	if len(block_starts) < 2 or len(block_starts) > 7:
		return None

	blocks = []
	for i in range(func_start, func_end, 4):
		try:
			insn = md.disasm(binstring[i:i+4], i).next()
		except StopIteration:
			break
		if i in block_starts:
			blocks.append([])
		blocks[-1].append(insn)

	argsblock = None
	for block in blocks[::-1]:
		if block[-1].mnemonic == 'bl':
			argsblock = block
			break
	if not argsblock:
		return None
	process_function = argsblock[-1].operands[0].value.imm
	process_function = plt_lookup.get(process_function, process_function)
	if not is_process_function(binstring, process_function):
		#print 'not_process_function'
		return None

	# keep it simple by skipping all instructions that do not generate immediates
	pos = 0
	while (pos < len(argsblock) and
		   argsblock[pos].mnemonic in ('stp', 'mov', 'str', 'add', 'ldr', 'and', 'ldp') and
		   'wzr' not in argsblock[pos].op_str):
		pos += 1

	result = get_last_immediate_argument(block[pos:])
	#if result is None:
	#	print block[pos:]

	return result, process_function

import sys

def shorten(s):
	for i in ('nn::sf::hipc::detail::', 'nn::sf::hipc::client::', 'nn::sf::cmif::client::', 'nn::sf::cmif::detail::', 'std::__1::', 'nn::sf::'):
		s = s.replace(i, '')
	return s

def get_method_info_part(s):
	start = s.index('CoreMethodInfo<') + len('CoreMethodInfo<')
	p = start
	depth = 1
	while depth:
		if s[p] == '>':
			depth -= 1
		elif s[p] == '<':
			depth += 1
		p += 1
	return s[start:p-1]

def hexify(s):
	def matchfunc(o):
		v = int(o.group(1))
		if v < 10:
			return '%d' % v
		else:
			return '0x%X' % v
	return re.sub('([0-9]+)u?l?', matchfunc, s)

def get_display_method_info(name):
	tup, inbytes, outbytes, sendpid = hexify(shorten(get_method_info_part(demangle(name)))).rsplit(', ', 3)
	tup = tup[6:-1].strip().replace('ArgumentInfo<', '<').replace(', ', ',').replace('>,', '>, ')
	parts = [inbytes + ' bytes in', outbytes + ' bytes out']
	if sendpid == 'true':
		parts.append('takes pid')
	if tup:
		parts.append(tup)
	return ' - '.join(parts)


def get_method_data(name):
	tup, inbytes, outbytes, sendpid = hexify(shorten(get_method_info_part(demangle(name)))).rsplit(', ', 3)

	tup = tup[6:-1].strip().replace('ArgumentInfo<', '<').replace(', ', ',').replace('>,', '>, ')

	data = {}
	data["inbytes"] = int(inbytes,16)
	data["outbytes"] = int(outbytes,16)
	if sendpid == 'true':
		data["pid"] = True

	data['arginfo'] = tup
	return data

def get_cmd_id_hash(vt):
	return hashlib.sha224(','.join('%d' % i for i in vt if i is not None)).hexdigest()[:8]


class IpcClientVtableEntry(object):
	def __init__(self, cmd, process_function, funcptr):
		self.cmd = cmd
		self.process_function = process_function
		self.funcptr = funcptr


class IpcClientVtable(object):
	def __init__(self, start, end, interface, entries, is_domain):
		self.start = start
		self.end = end
		self.interface = interface
		self.entries = entries
		self.is_domain = is_domain


def iter_vtables_in_nxo(f):
	assert f.textoff == 0
	f.binfile.seek(f.textoff)
	binstring = f.binfile.read(f.dataoff + f.datasize)


	fptr_syms = {}
	data_syms = {}
	for offset, r_type, sym, addend in f.relocations:
		if f.dataoff <= offset < f.dataoff + f.datasize:
			if sym and sym.shndx and sym.value < f.textsize:
				fptr_syms[offset] = sym.value
			elif addend and addend < f.textsize:
				fptr_syms[offset] = addend
			elif sym and sym.shndx and sym.value:
				data_syms[offset] = sym.value
			elif addend:
				data_syms[offset] = addend

	#print hex(f.dataoff), f.dataoff < 0xCE7AA8
	#print struct.unpack_from('<q', binstring, 0xCE7AA8)[0]
	for i in range(f.dataoff, len(binstring), 8):
		#print hex(i), hex(len(binstring))
		value = struct.unpack_from('<q', binstring, i)[0]
		if value in (-0x10, -0x20):
			#if i == 0xCE7AA8:
			#	print hex(i)
			end = i
			start = end
			while start - 8 in fptr_syms:
				start -= 8

			process_functions = [None] * ((end-start)/8)

			vt = []
			funcptrs = []
			for j in range(start, end, 8):
				entry = fptr_syms[j]
				cmd_id = get_function_cmd_id(binstring, entry, f.plt_lookup, f.rodataoff, f.dataoff)
				if cmd_id is not None:
					cmd_id, process_function = cmd_id
					process_functions[(j-start)/8] = process_function
				vt.append(cmd_id)
				funcptrs.append(entry)


			if len(vt) > 4 and all(i is None for i in vt[:4] + vt[-1:]) and not any(i is None for i in vt[4:-1]):
				interface = ''
				raw_vtable_name = ''
				if start-8 in data_syms:
					rtti_string = data_syms[data_syms[start-8]+8]
					raw_vtable_name = binstring[rtti_string:binstring.index('\0',rtti_string)]
					interface = demangle(raw_vtable_name)
				elif start-16 in f.addr_to_name:
					raw_vtable_name = f.addr_to_name[start-16]
					interface = demangle(raw_vtable_name)
				else:
					interface = 'IUnknown_%s_0x%X' % (get_cmd_id_hash(vt), start + IDA_BASE)
					interface = MANUAL_NAME_LOOKUP.get(interface, interface)

				is_domain = False
				if 'CmifDomainProxy' in raw_vtable_name:
					is_domain = True

				entries = []
				for cmd, process_function, funcptr in zip(vt, process_functions, funcptrs):
					entries.append(IpcClientVtableEntry(cmd, process_function, funcptr))
				yield IpcClientVtable(start, end, interface, entries, is_domain)


def dump_vtables(fname):
	with open(fname, 'rb') as li:
		f = load_nxo(li)

	#for name in  '_nn_sf_sync_' 
	for vtable in iter_vtables_in_nxo(f):
		#print '?'
		#continue
		print '  %r: {' % vtable.interface
		for entry in vtable.entries:
			if entry.cmd is not None:
				data = {}
				if entry.funcptr in f.addr_to_name:
					demangled = demangle(f.addr_to_name[entry.funcptr])
					name, args = demangled.split('>::_nn_sf_sync_')[-1].split('(', 1)
					args = args[:-1]
					#parts.append('%r: %r' % ('name', name))
					#parts.append('%r: %r' % ('args', args))
					data['name'] = name
					data['args'] = shorten(args)


				if entry.process_function is not None and entry.process_function in f.addr_to_name:
					#parts.append('%r: %r' % ('data', ))
					data.update(get_method_data(f.addr_to_name[entry.process_function]))
					#s += (' | ' + )

				parts = []
				for i in ['inbytes', 'outbytes', 'name', 'pid', 'args', 'arginfo']:
					if i not in data: continue
					v = data[i]
					if isinstance(v, (list, bool, str)):
						v = repr(v)
					else:
						if v >= 10:
							v = '0x%X' % v
						else:
							v = str(v)
						v = v.rjust(5)
					parts.append('"%s": %s' % (i, v))
				print '    %5d: {%s},' % (entry.cmd, ', '.join(parts))

		print '  },'


#from wherever import namez # or just paste it here

def dump_structs(fname):
	with open(fname, 'rb') as li:
		f = load_nxo(li)
		#for k,v in namez.iteritems():
		#	f.

	for vtable in iter_vtables_in_nxo(f):
		interface = vtable.interface

		#if 'CmifDomainProxy' in tail:
		#	interface += '::DomainProxy'

		print
		print 'struct %s;' % interface

		print 'struct %s::vt' % interface
		print '{'
		for i, entry in enumerate(vtable.entries):
			if entry.cmd is not None:
				funcname = 'Cmd%d' % entry.cmd
				if entry.funcptr in f.addr_to_name:
					ipcname = demangle(f.addr_to_name[entry.funcptr]).split('>::_nn_sf_sync_')[-1].split('(')[0]
					funcname += '_' + ipcname					
			else:
				funcname = {
					0: 'AddReference',
					1: 'Release',
					2: 'GetProxyInfo',
					3: 'GetInterfaceTypeInfo',
				}.get(i)
				if funcname is None:
					if i == len(vtable.entries) - 1:
						funcname = 'GetCmifBaseObject'
					else:
						funcname = 'func%X' % (i * 8)
			print '  _DWORD (*__fastcall %s)(%s *this, ...);' % (funcname, interface)

		print '};'
		print 'struct %s' % interface
		print '{'
		print '  %s::vt *_vt;' % interface
		print '  _BYTE byte8;'
		print '  _BYTE byte9;'
		print '  unsigned int handle;'
		print '  void *_vt10;'
		print '  _DWORD dword18;'
		print '  _QWORD qword20;'
		print '};'



def dump_unique_ids(fnames):
	all_cmds = set()
	for fname in sys.argv[1:]:
		with open(fname, 'rb') as li:
			f = load_nxo(li)
		new = False
		for vtable in iter_vtables_in_nxo(f):
			interface = vtable.interface

			for i, entry in enumerate(vtable.entries):
				if entry.cmd is not None and entry.cmd not in all_cmds:
					print entry.cmd
					new = True
					all_cmds.add(entry.cmd)
		if new:
			print all_cmds


def main():
	dump_vtables(sys.argv[1])
	#dump_structs(sys.argv[1])
	#dump_unique_ids(sys.argv[1:])
	#for fname in sys.argv[1:]:
	#	dump_structs(fname)


if __name__ == '__main__':
	main()


