import sys
import re
import nxo64

def main(pattern, filename):
	f = nxo64.load_nxo(open(filename, 'rb'))

	f.binfile.seek(0)
	target_text = f.binfile.read(f.textsize)

	rows = eval('[' + open(pattern).read() + ']')
	with open(filename + '-sdk-syms.py', 'wb') as f:

		f.write('syms = [\n')
		for value, size, regex, name in rows:
			#print '(0x%X, 0x%X, %r, %r),' % (sym.value, sym.size, regex, sym.name)
			positions = [m.start() for m in re.finditer(regex, target_text)]
			if len(positions) == 1:
				f.write('(0x%X, %r),\n' % (0x7100000000 + positions[0], name))
		f.write(''']

for addr, sym in syms:
	oldname = Name(addr)
	if oldname.startswith('sub_'):
		MakeName(addr, sym)
		MakeComm(addr, 'name from regex match')
	elif oldname.startswith('loc_'):
		MakeName(addr, sym)
		MakeComm(addr, 'name from regex match')
		print '%X %s %s' % (addr, oldname, sym)
	elif oldname != sym:
		print '%X %s %s' % (addr, oldname, sym)
''')

			
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'usage: applypattern.py pattern.txt [nxo files...]'
		print 'writes output to input filename + "-sdk-syms.py"'
	for filename in sys.argv[2:]:
		main(sys.argv[1], filename)
