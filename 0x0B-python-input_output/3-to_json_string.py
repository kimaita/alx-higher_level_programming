#!/usr/bin/python3
"""This module contains a function for JSON conversion"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string):

    Args:
        my_obj (Any):object to serialize
    """
    return json.dumps(my_obj)
