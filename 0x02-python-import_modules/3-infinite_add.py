#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    no = len(argv) - 1
    j = 0
    for i in range(0, no):
        j += int(argv[i + 1])
    print("{}".format(j))
