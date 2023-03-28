#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints `x` elements of a list.

    Args:
        my_list: List containing elements to print. Defaults to [].
        x: Number of elements to print. Defaults to 0.
    Returns:
        the real number of elements printed
    """
    try:
        i = 0
        while i < x:
            print(my_list[i], end='')
            i += 1
        print()
        return i
    except IndexError:
        print()
        return i
