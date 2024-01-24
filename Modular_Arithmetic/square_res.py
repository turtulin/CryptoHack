from Crypto.Util.number import *

p = 29
ints = [14, 6, 11]

for a in range(1, p):
    if(a ** 2) % p in ints:
        print(a)