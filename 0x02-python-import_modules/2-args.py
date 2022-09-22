#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    no = len(argv) - 1
    if no == 0:
        print("{:d} arguments.".format(no))
    elif no == 1:
        print("{:d} argument:".format(no))
    else:
        print("{:d} arguments:".format(no))
    for i in range(0, no):
        print("{:d}: {}".format((i + 1), argv[(i + 1)]))
