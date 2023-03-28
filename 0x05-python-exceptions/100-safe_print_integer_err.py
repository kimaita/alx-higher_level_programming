#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer.

    Args:
        value: variable to print
    Returns:
        `True` if `value` correctly printed i.e `value` is an integer

        `False` otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
