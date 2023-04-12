#!/usr/bin/python3
"""This module contains a function for opening and reading files"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout

    Args:
        filename (str): Name of the fie. Defaults to "".
    """
    if filename:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            if text:
                print(text)
