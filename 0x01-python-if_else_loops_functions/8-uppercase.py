#!/usr/bin/python3
def uppercase(str):
    len_s = len(str)
    for i in range(0, len_s):
        asc = ord(str[i])
        if asc > 64 and asc < 91:
            asc = asc
        elif asc > 96 and asc < 123:
            asc = asc - 32
        if i != len_s - 1:
            print("{:c}".format(asc), end = '')
        else:
            print("{:c}".format(asc))
