#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c > 96 and c < 123:
        print("{:c} is lower".format(c))
        return (True)
    elif c >66 and c < 91:
        print("{:c} is upper".format(c))
        return (False)
