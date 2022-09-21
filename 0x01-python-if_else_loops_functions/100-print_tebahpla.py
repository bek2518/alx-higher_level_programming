#!/usr/bin/python3
for i in range(-122, -96):
    i = -i
    if (i % 2) == 0:
        print("{:c}".format(i), end='')
    elif (i % 2) != 0:
        i = i - 32
        print("{:c}".format(i), end='')
