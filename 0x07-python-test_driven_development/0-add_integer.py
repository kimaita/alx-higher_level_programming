#!/usr/bin/python3
"""This module contains a single function for integer addition.
"""


def add_integer(a, b=98):
    """Adds two integers/floats

    If a float is provided, it is first cast into an integer

    Args:
        a (int/float): The first number
        b (int/float, optional): The second number. Defaults to 98.

    Returns:
        sum of `a` and `b`
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)

    return a+b
