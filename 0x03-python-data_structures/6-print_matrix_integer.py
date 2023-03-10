def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers given a list of lists

    Args:
        matrix: lists of lists. Defaults to [[]].
    """
    for row in matrix:
        i = 0
        row_len = len(row)-1
        for item in row:
            end = ' ' if i != row_len else ''
            print('{:d}'.format(item), end=end)
            i += 1
        print('')
