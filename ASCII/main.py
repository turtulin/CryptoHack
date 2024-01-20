import array


def int2ascii(array):
    flag = ""
    for number in array:
        c = chr(number)
        flag += c
    return flag


if __name__ == '__main__':
    a = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    print(int2ascii(a))
