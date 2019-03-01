import sys
import re
from nxo64 import load_nxo

SEARCH_ALL_SECTIONS = False

def main(filenames):
	for filename in filenames:
		try:
			with open(filename, 'rb') as li:
				f = load_nxo(li)
		except Exception as e:
			print filename, e
			continue
		if SEARCH_ALL_SECTIONS:
			f.binfile.seek(0)
			as_string = f.binfile.read_to_end()
		else:
			f.binfile.seek(f.rodataoff)
			as_string = f.binfile.read(f.rodatasize)
		strs = re.finditer(r'[ -~]{5,}', as_string)
		for i in strs:
			start = i.start() + f.rodataoff + 0x7100000000
			print '%s(%X): %s' % (filename, start, i.group(0))

if __name__ == '__main__':
    main(sys.argv[1:])