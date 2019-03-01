import sys
import struct

from nxo64 import load_nxo, STT_FUNC
import arm64

def main(filenames):
	import re

	with open(filenames[0], 'rb') as li:
		f = load_nxo(li)

	f.binfile.seek(0)
	textstr = f.binfile.read(f.textsize)


	important = set()
	for sym in f.symbols:
		if sym.type != STT_FUNC: continue
		if sym.shndx and sym.value and sym.size:
			adrp_regs = set()
			mask = [0xFFFFFFFF for i in range(0, sym.size, 4)]


			f.binfile.seek(sym.value)
			instrs = [f.binfile.read('I') for i in range(0, sym.size, 4)]

			for i, instr in enumerate(instrs):
				if arm64.is_ADRP_only_pcreladdr(instr):
					mask[i] &= ~((0x7FFFF << 5) | (3 << 29))
					adrp_regs.add(arm64.get_Rd(instr))

				if arm64.is_branch_imm(instr):
					target = (i + arm64.get_imm26_s(instr)) * 4 
					if target < 0 or target >= sym.size:
						mask[i] &= ~0x3FFFFFF

			if adrp_regs:
				for i, instr in enumerate(instrs):
					if arm64.is_ADD_64_addsub_imm(instr):
						mask[i] &= ~(0xFFF << 10)

					# not sure if valid, would fail on adrp / mov / add
					if arm64.is_ldst_pos(instr):
						if arm64.get_Rn(instr) in adrp_regs:
							mask[i] &= ~(0xFFF << 10)

			mask_str = ''.join(struct.pack('<I', m) for m in mask)
			bits = ''.join(struct.pack('<I', i&m) for i,m in zip(instrs, mask))
			regex = ''.join((re.escape(i) if m == '\xFF' else r'[\0-\xff]') for i, m in zip(bits, mask_str))

			positions = [m.start() for m in re.finditer(regex, textstr)]
			assert len(positions) >= 1, hex(sym.value + 0x7100000000)
			if len(positions) > 1:
				pass

			if len(positions) == 1: # probably good?
				print '(0x%X, 0x%X, %r, %r),' % (sym.value, sym.size, regex, sym.name)


if __name__ == '__main__':
	main(sys.argv[1:])
