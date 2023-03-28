#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first `x` elements of a list and only integers

    Args:
            my_list: list of items to print. Defaults to [].
            x: number of elements to access in `my_list`. Defaults to 0.
    Return:
            the real number of integers printed
    """
    i, printed = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print('')
    return printed
