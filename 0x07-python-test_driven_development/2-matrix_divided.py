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
            If matrix is not a a list
            If elements of matrix list are not integers
            If each row of the matrix doesnot have the same size
            If div is not a number(int/float)

        ZeroDivisionError: if div == 0
    '''
    msg_m = "matrix must be a matrix (list of lists) of integers/floats"
    msg_r = "Each row of the matrix must have the same size"

    new_list = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError(msg_m)
    for i in range(len(matrix)):
        if (len(matrix[i]) != len(matrix[0])):
            raise TypeError(msg_r)
        inner_list = []
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(msg_m)
            else:
                inner_list.append(round(matrix[i][j] / div, 2))
        new_list.append(inner_list)
    return (new_list)
