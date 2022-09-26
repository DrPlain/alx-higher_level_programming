#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i, element in enumerate(matrix):
        for j, element in enumerate(matrix[i]):
            print("{:d}".format(matrix[i][j]), end=' ' if j < (
                len(matrix[i])-1) else '')
        print()
