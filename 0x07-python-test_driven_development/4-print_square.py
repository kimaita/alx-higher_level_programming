#!/usr/bin/python3
"""This module contains a function for printing a square
"""


def print_square(size):
    """Prints a square of dimensions `size` with the character `#`
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#'*size, end='')
        print('')
