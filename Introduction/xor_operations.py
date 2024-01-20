from pwn import *

hex_1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
hex_1_2 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
hex_2_3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
hex_F = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key_1 = bytes.fromhex(hex_1)
bytes_1_2 = bytes.fromhex(hex_1_2)
key_2 = xor(key_1, bytes_1_2)
bytes_2_3 = bytes.fromhex(hex_2_3)
key_3 = xor(bytes_2_3, key_2)
bytes_F = bytes.fromhex(hex_F)
flag = xor(key_1, key_2, key_3, bytes_F)
print(flag)