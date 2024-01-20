from pwn import *

hex = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
bytes = bytes.fromhex(hex)
key = xor(bytes[:7], 'crypto{') + xor(bytes[-1], '}')
print(key)
flag = xor(bytes, key)
print(flag)
