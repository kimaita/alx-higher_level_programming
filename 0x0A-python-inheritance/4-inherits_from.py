#!/usr/bin/python3
"""This module contains a function for checking class inheritance"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
    (directly or indirectly) from a specified class

    Args:
        obj (str): the object
        a_class (str): name of the class
    Returns:
        True if `obj` inherits from `a_class`, False otherwise
    """
    return issubclass(obj.__class__, a_class) and not obj.__class__ == a_class
