#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    no = len(sys.argv) - 1
    if no != 3:
        print(f'Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print(f'Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op == '+':
        print(f'{a} + {b} = {add(a, b)}')
    elif op == '-':
        print(f'{a} - {b} = {sub(a, b)}')
    elif op == '*':
        print(f'{a} * {b} = {mul(a, b)}')
    else:
        print(f'{a} / {b} = {div(a, b)}')
