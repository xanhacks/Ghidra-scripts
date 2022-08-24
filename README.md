# Ghidra scripts

You can add Python script to [Ghidra](https://ghidra-sre.org/) (software for reverse engineering).

Ghidra API and Python helps you automate some reverse engineering tasks.

## Installation

1. Create a folder at `~/ghidra_scripts` and move Python scripts in it.
2. Inside Ghidra, go to `Window -> Script Mananger`.
3. In the toolbar, click on `Manage Sript Directories` and enable `$USER_HOME/ghidra_scripts`.
4. Now you can search for your scripts with the search bar and double click on it to run it.

## Scripts

### find\_xor\_with\_different\_registers.py

Find all the XOR opcode with operand 1 not equals to operand 2 inside the `.text` section.

Example :

```
find_xor_with_different_registers.py> Running...
[INFO] You can click on address to view it in the dissasembler (listing) view.
[INFO] Looking for XOR ...
[INFO] 0x08048cd8 : XOR EAX,0x30
[INFO] 0x08048e30 : XOR EDI,dword ptr GS:[0x14]
[INFO] Done !
find_xor_with_different_registers.py> Finished!
```

## Ressources

- [HackOvert/GhidraSnippets](https://github.com/HackOvert/GhidraSnippets)
