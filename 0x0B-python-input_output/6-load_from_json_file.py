#!/usr/bin/python3
"""This module contains a function for JSON file reading"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename (str): name of JSON file
    """
    with open(filename, 'r', encoding='utf-8') as fp:
        obj = json.load(fp)
    return obj
