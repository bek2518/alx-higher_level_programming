#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix = matrix[i]
            if j != (len(matrix[i]) - 1):
                print("{} ".format(new_matrix[j]), end='')
            else:
                print("{}$".format(new_matrix[j]), end='')
        print()
