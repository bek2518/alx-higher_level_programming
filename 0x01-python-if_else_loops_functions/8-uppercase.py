#!/usr/bin/python3
def uppercase(str):
    len_s = len(str)
    for i in range(0, len_s):
        asc = ord(str[i])
        if asc >= 97 and asc <= 122:
            asc = asc - 32
        else:
            asc = asc
        print("{:c}".format(asc), end='')
    print()
uppercase("z")
uppercase("Holberton")
