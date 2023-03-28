#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with `"{:d}".format()`

    Args:
        value: variable to print
    Returns:
        * `True` if `value` has been correctly printed i.e. it is an integer
        * `False` otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
