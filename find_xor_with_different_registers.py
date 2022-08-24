#Find all the XOR opcode where "operand 1 != operand 2" in the .text section.
#@author xanhacks
#@category Search
#@keybinding Ctrl-X


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

