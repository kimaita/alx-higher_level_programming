#!/usr/bin/python3
"""This module contains a function for JSON deserialization"""
import json


def from_json_string(my_str):
    """Returns a Python object from a JSON string

    Args:
        my_str (_type_): SON  string to deserialize
    """
    return json.loads(my_str)
