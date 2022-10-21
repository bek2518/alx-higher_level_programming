#!/usr/bin/python3
'''
Module that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    Function that divides a matrix(list of lists)

    Args:
        matrix:
        div:

    Return: new matrix

    Raises:
        TypeError: 
        ZeroDivisionError: if div == 0
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i, j], int) and not isinstance(matrix[i, j], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/float")
    for i in range(len(matrix) - 1)
        if (len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix / div
