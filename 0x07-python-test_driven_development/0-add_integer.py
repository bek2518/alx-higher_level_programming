#!/usr/bin/python3
'''
Module with a function that adds two numbers
'''


def add_integer(a, b=98):
    '''
    Function that adds two integers

    Args:
        a: first integer
        b: second integer

    Return:
        Addition of the two numbers

    Raise:
        TypeError: if a and b are not integers
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return(a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.txt")
