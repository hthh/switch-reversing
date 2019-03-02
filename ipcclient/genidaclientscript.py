import sys

from nxo64 import load_nxo
from ipcclient import iter_vtables_in_nxo, demangle

IDA_BASE = 0x7100000000

def gen_ida_script(fname):
	with open(fname, 'rb') as li:
		f = load_nxo(li)

	print '# output of genidaclientscript.py'
	print r'''
already_named = set()
def client_vtable(interface, vtstart, vtend, names):
	global already_named
	if interface in already_named:
		return # TODO
	already_named.add(interface)
	vtname = interface + '::vt'

	vtoldname = Name(vtstart)
	if not vtoldname or vtoldname.startswith('off_'):
		MakeName(vtstart, interface + '::vtable')

	print 'struct %s;' % interface
	print 'struct %s { /* %x-%x */' % (vtname, vtstart, vtend)

	for vtea, funcname in zip(range(vtstart, vtend, 8), names):
		funcea = Qword(vtea)
		cfunc = idaapi.decompile(funcea)
		functype = str(cfunc.type)

		if functype.count('__fastcall') == 0:
			ret, args = functype.split('(', 1)
			args = '(' + args
		else:
			assert functype.count('__fastcall') == 1,  '%X %s' % (funcea, functype)
			ret, args = functype.split('__fastcall')

		if 'Cmd' in funcname:
			ret = 'unsigned int '

		args = args[1:-1].split(',')
		args = [interface + ' *this'] + args[1:]

		if '::DomainProxy::' in funcname:
			name = funcname.split('::')[-3] + '_' + funcname.split('::')[-1]
		else:
			name = '_'.join(funcname.split('::')[-2:])

		functype = ret + '(*__fastcall ' + name + ')' + '(' + ','.join(args) + ')'

		functype = functype.replace(', double a2, double a3, double a4, double a5, double a6, double a7, double a8, double a9', '')
		print '  /* %X */ %s;' % (funcea, functype)
	print '};'
	print 'struct %s {' % interface
	print '  %s *_v;' % vtname
	print '  _BYTE byte8;'
	print '  _BYTE byte9;'
	print '  unsigned int handle;'
	print '  void *_vt10;'
	print '  _DWORD dword18;'
	print '  _QWORD qword20;'
	print '};'

'''
	print '# decompile all process functions first'
	already_decompiled = set()

	vtables = []
	for vtable in iter_vtables_in_nxo(f):
		vtables.append(vtable)
		for i, entry in enumerate(vtable.entries):
			if entry.process_function and entry.process_function not in already_decompiled:
				print 'idaapi.decompile(0x%X)' % (IDA_BASE + entry.process_function)
				already_decompiled.add(entry.process_function)

	for vtable in vtables:
		interface = vtable.interface
		if vtable.is_domain:
			interface += '::DomainClient'
		else:
			interface += '::Client'

		names = []
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
			names.append(funcname)

		if 'IUnknown' in interface: continue
		print 'client_vtable(%r, 0x%X, 0x%X, %r)' % (interface, IDA_BASE+vtable.start, IDA_BASE+vtable.end, names)



def main():
	for fname in sys.argv[1:2]:
		gen_ida_script(fname)


if __name__ == '__main__':
	main()
