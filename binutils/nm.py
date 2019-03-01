import sys
import re
from nxo64 import load_nxo

def visibility_str(vis):
	return [
		'DEFAULT  ', # Default symbol visibility rules
		'INTERNAL ', # Processor specific hidden class
		'HIDDEN   ', # Sym unavailable in other modules
		'PROTECTED', # Not preemptible, not exported
	][vis]

def type_str(t):
	return {
		0: 'NOTYPE ', # Symbol type is unspecified
		1: 'OBJECT ', # Symbol is a data object
		2: 'FUNC   ', # Symbol is a code object
		3: 'SECTION', # Symbol associated with a section
		4: 'FILE   ', # Symbol's name is file name
		5: 'COMMON ', # Symbol is a common data object
		6: 'TLS    ', # Symbol is thread-local data object
	}.get(t, 'type=%-2d'%t)

def bind_str(b):
	return {
		0: 'LOCAL ',
		1: 'GLOBAL',
		2: 'WEAK  ',
	}.get(b, 'bind%d' % b)

def as_int16(v):
	v &= 0xFFFF
	if v & 0x8000:
		v |= ~0xFFFF
	return v

def main(filenames):
	for filename in filenames:
		with open(filename, 'rb') as li:
			f = load_nxo(li)

		for s in sorted(f.symbols, key=lambda sym: sym.value):
			line = ''
			value = s.value
			if s.shndx or s.value:
				line += '%08x ' % (s.value,)
				if value < f.rodataoff:
					line += 'T'
				elif value < f.dataoff:
					line += 'R'
				elif value < f.bssoff:
					line += 'D'
				elif value < f.bssoff + f.bsssize:
					line += 'B'
				else:
					line += '?'
				line += ' '
			else:
				line += ' ' * 11

			line += '%s ' % (visibility_str(s.vis),)
			line += '%s ' % (type_str(s.type),)
			line += '%s ' % (bind_str(s.bind),)
			line += '%3d ' % (as_int16(s.shndx),)
			line += '%8x ' % (s.size,)
			line += '%s' % (s.name,)
			print line

if __name__ == '__main__':
    main(sys.argv[1:])