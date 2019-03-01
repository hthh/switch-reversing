import sys
import struct
import re
from nxo64 import load_nxo

def main(filenames):
	for filename in filenames:
		print 'File:', filename
		with open(filename, 'rb') as li:
			f = load_nxo(li)

		path = None
		for off, end, name, class_ in f.sections:
			if name == '.rodata' and end-off < 0x1000 and end-off > 8:
				id_ = f.binfile.read_from(end-off, off)
				length = struct.unpack_from('<I', id_, 4)[0]
				if length + 8 <= len(id_):
					id_ = id_[8:length + 8]
					path = id_
				break

		f.binfile.seek(f.rodataoff)
		as_string = f.binfile.read(f.rodatasize)

		if path is None:
			strs = re.findall(r'[a-z]:[\\/][ -~]{5,}\.n[rs]s', as_string, flags=re.IGNORECASE)
			if strs:
				path = strs[-1]

		if path is not None:
			print 'Module:', path
		print '%d-bit' % (32 if f.armv7 else 64,)
		sdk_version = re.findall(r'sdk_version: ([0-9.]*)', as_string)
		if sdk_version:
			print 'FS SDK Version:', sdk_version[0]

		symbol_count = 0
		for s in f.symbols:
			if s.shndx and s.name:
				symbol_count += 1
		print 'Number of Symbols:', symbol_count

		for i in re.findall(r'SDK MW[ -~]*', as_string):
			print i
		print

if __name__ == '__main__':
	main(sys.argv[1:])