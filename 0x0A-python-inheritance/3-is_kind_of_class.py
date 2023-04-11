#!/usr/bin/python3
"""This module contains a function that checks an object's class"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of a class, or an instance of an
    inherited class.

    Args:
        obj (Any): Object to check
        a_class (str): the class to check against

    Returns:
        True if `obj` is an instance of `a_class` or an inherited class,
        False otherwise
    """
    return isinstance(obj, a_class)
