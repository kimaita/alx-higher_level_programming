#!/usr/bin/python3
"""This module contains a function for JSON file writing"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation

    Args:
        my_obj (Any): object to write to JSON file
        filename (str): name of JSON file
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
