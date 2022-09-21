#!/usr/bin/python3
def remove_char_at(str, n):
    strn = str
    for i in range(0, len(strn)):
        if i != n:
            print("{:c}".format(ord(strn[i])), end='')
print()
