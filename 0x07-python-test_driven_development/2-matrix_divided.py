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

    if not isinstance(matrix, [[]])
