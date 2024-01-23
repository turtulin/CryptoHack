a = 66528
b = 52920

while b > 0:
    r = a % b
    a, b = b, r

print(a)