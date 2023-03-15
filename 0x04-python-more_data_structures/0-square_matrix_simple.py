#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Squares each element of the given matrix

    Args:
        matrix: list of lists. Defaults to [].

    Returns:
        matrix with all elements squared
    """
    return [[x**2 for x in row] for row in matrix]
