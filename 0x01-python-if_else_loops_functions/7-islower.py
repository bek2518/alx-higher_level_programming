#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c > 96 and c < 123:
        return (True)
    elif c > 66 and c < 91:
        return (False)
