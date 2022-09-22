#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    no = len(argv) - 1
    if no != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    op = argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)
    a = int(argv[1])
    b = int(argv[3])
    if op == '+':
        print("{:d} {:c} {:d} = {:d}".format(a, ord(op), b, add(a, b)))
    elif op == '-':
        print("{:d} {:c} {:d} = {:d}".format(a, ord(op), b, sub(a, b)))
    elif op == '*':
        print("{:d} {:c} {:d} = {:d}".format(a, ord(op,) b, mul(a, b)))
    elif op == '/'
        print("{:d} {:c} {:d} = {:d}".format(a, ord(op), b, div(a, b)))
