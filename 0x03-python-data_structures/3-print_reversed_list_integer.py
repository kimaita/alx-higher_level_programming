def print_reversed_list_integer(my_list=[]):
    """Prints integers in a list in reverse order

    Each integer is printed on a new line

    Args:
        my_list: list to print. Defaults to [].
    """
    for i in my_list[::-1]:
        print('{:d}'.format(i))
