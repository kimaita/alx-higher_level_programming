#!/usr/bin/python3
"""This module contans a function to compare object types"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class

    Args:
        obj (Any): The object to check
        a_class (Any): The class to check against

    Returns:
        True if `obj` is exactly an instance of `a_class`, `False` otherwise
    """
    return obj.__class__ == a_class
