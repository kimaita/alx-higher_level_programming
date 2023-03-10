def print_list_integer(my_list=[]):
    """Prints integers in a list

    Each integer is printed on a new line

    Args:
        my_list: list to print. Defaults to [].
    """
    for i in my_list:
        print('{:d}'.format(i))
