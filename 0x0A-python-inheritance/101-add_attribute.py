#!/usr/bin/python3
"""This module contains a function for altering objects"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object.

    Args:
        obj (Any): object to add attribute
        name (str): name of attribute
        value (Any): value of attribute

    Raises:
        TypeError: if the attribute cannot be added
    """
    try:
        setattr(obj, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
