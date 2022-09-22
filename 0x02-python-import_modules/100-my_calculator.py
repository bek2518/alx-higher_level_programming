#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    no = len(sys.argv) - 1
    if no != 3:
        print("Usage: ./100-mycalculator.py <a> <operator> <b>")
        exit (1)
    a = int(sys.argv[1])
    operator = ord(sys.argv[2])
    b = int(sys.argv[3])
    if operator == 43:
        print("{} {:c} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == 45:
        print("{} {:c} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == 42:
        print("{} {:c} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == 47:
        print("{} {:c} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit (1)
