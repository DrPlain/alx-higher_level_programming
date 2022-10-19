#!/usr/bin/python3
"""Contains the function matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div
    Args:
        matrix(list of lists): Elements must be integers or floats
        div: The divisor, must be a number

    Raises:
        TypeError:
            1. if matrix is not a list of lists of integers or floats
            2. If all rows of matrix are not the same size
            3. If div is not a number

        ZeroDivisionError: If div is 0

    Returns: Returns a new matrix containing the quotients
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    res_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for ele in row:
            if not isinstance(ele, int) and not isinstance(ele, float):
                raise TypeError(err_msg)
        res_matrix.append(list(map(lambda ele: (round(ele / div, 2)), row)))
    return res_matrix
