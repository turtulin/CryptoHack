from pwn import *

puzzle = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
bytes_puzzle = bytes.fromhex(puzzle)
for i in range(256):
    flag = xor(bytes_puzzle, i)
    print(flag)