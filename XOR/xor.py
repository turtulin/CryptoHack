from pwn import *

s = 'label'
n = 13
print(xor(s, n))