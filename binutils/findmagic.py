import sys
import struct
import re
from nxo64 import load_nxo

def get_hw(d): return (d >> 21) & 3
def get_imm16(d): return (d >> 5) & 0xFFFF

def is_MOVZ_32_movewide(d): return (d & 0xff800000) == 0x52800000
def is_MOVK_32_movewide(d): return (d & 0xff800000) == 0x72800000
def get_Rd(d): return (d >> 0) & 0x1F

def main(magicstr, filenames):
	for filename in filenames:
		find_magic(magicstr, filename)

def find_magic_in_file(filename, text, data_as_string, f, magic):

	magic_high = magic >> 16
	magic_low = magic & 0xFFFF

	load_base = 0x7100000000

	for i in xrange(0, len(text), 4):
		d = struct.unpack_from('<I', text, i)[0]
		if magic_high:
			if is_MOVZ_32_movewide(d) and get_hw(d) == 1 and get_imm16(d) == magic_high:
				print '%s(%X): MOVZ W%d, 0x%X # %r' % (filename, load_base + i, get_Rd(d), magic_high << 16, struct.pack('<H', magic_high))
			if is_MOVK_32_movewide(d) and get_hw(d) == 0 and get_imm16(d) == magic_low:
				print '%s(%X): MOVK W%d, 0x%X # %r' % (filename, load_base + i, get_Rd(d), magic_low, struct.pack('<H', magic_low))
		else:
			if is_MOVZ_32_movewide(d) and get_hw(d) == 0 and get_imm16(d) == magic_low:
				print '%s(%X): MOVZ W%d, 0x%X # %r' % (filename, load_base + i, get_Rd(d), magic_low, struct.pack('<H', magic_low))

	pattern = struct.pack('<I', magic)
	strs = re.finditer(re.escape(pattern), data_as_string)
	for i in strs:
		start = i.start() + f.rodataoff + 0x7100000000
		print '%s(%X): DCD 0x%X # %s' % (filename, start, magic, pattern)

def find_magic(magicstr, filename):
	try:
		with open(filename, 'rb') as li:
			f = load_nxo(li)
	except Exception as e:
		print filename, e
		return
	f.binfile.seek(0)
	text = f.binfile.read(f.textsize)

	f.binfile.seek(f.rodataoff)
	data_as_string = f.binfile.read_to_end()

	if magicstr.startswith('0x'):
		magic = int(magicstr, 16)
		find_magic_in_file(filename, text, data_as_string, f, magic)
	else:
		for fmt in ('<I', '>I'):
			magic = struct.unpack(fmt, magicstr)[0]
			find_magic_in_file(filename, text, data_as_string, f, magic)

		#print hex(magic)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2:])