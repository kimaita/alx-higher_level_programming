#!/usr/bin/python3
"""This module contains a function for object->dict serialization"""


def class_to_json(obj):
    """Returns an object's dictionary

    Args:
        obj (Any): the object
    """
    return vars(obj)
