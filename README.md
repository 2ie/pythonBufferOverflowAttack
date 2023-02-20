Buffer overflow script made in Python.

Utilized shellcode taken from Aleph1's Smashing the stack for fun and profit.

This particular script only works in environments where address space layout randomization has been disabled, and takes advantage of memory vulnerabilities in C's strcpy function.
