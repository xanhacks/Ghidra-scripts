#Find XOR in .text section (except: xor REG1, REG1)
#@author xanhacks
#@category Search
#@keybinding Ctrl-X

# Docs : https://ghidra.re/ghidra_docs/api/ghidra/program/flatapi/FlatProgramAPI.html


if __name__ == "__main__":
	listing = currentProgram.getListing()
	func = getFirstFunction()
	entryPoint = func.getEntryPoint()
	instructions = listing.getInstructions(entryPoint, True)

	print("[INFO] You can click on address to view it in the dissasembler (listing) view.")
	print("[INFO] Looking for XOR ...")
	for instruction in instructions:
		addr = instruction.getAddress()
		oper = instruction.getMnemonicString()
		
		if oper.startswith("XOR") and instruction.getRegister(0) != instruction.getRegister(1):
		    print("[INFO] 0x{} : {}".format(addr, instruction))
	print("[INFO] Done !")

