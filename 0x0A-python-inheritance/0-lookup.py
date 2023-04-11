#!/usr/bin/python3
"""This module contains a funcion for obtaining an object's attributes
"""


def lookup(obj):
    """Derives all available attribues and methods of an object
    Args:
        obj (Any): The object to describe

    Returns:
        List of obj's attributes
    """
    return dir(obj)
