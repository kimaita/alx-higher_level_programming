#!/usr/bin/python3
"""This modules defines a function for element-wise division of a matrix
and a helper function for raising a specific exception with its detail
"""


def matrix_divided(matrix, div):
    """Divides each element in a matrix by a number

    Args:
        matrix: list of lists of numbers
        div: number to divide matrix elements by

    Returns:
        a new matrix of the quotients
    """
    if not isinstance(matrix, list):
        raise_matrix_error()

    len_first = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list) or not len(row):
            raise_matrix_error()
        if len(row) != len_first:
            raise TypeError('Each row of the matrix must have the same size')
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise_matrix_error()

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div:
        return [[round(i/div, 2) for i in row] for row in matrix]
    else:
        raise ZeroDivisionError('division by zero')


def raise_matrix_error():
    """Raises a TypeError."""
    raise TypeError(
        'matrix must be a matrix (list of lists) of integers/floats')
