#!/usr/bin/python3
'''
Module that prints a square with character #
'''


def print_square(size):
    '''
    Prints square using # character

    Args:
        size: size length of the square

    Raises:
        TypeError: If size is not an integer
                    If size is float and is less than 0
        ValueError: If size less than 0
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
