#!/usr/bin/python3
"""This module defines a function for writing to a file"""


def append_write(filename="", text=""):
    """Appends a string to a text file

    Args:
        filename (str): name of file to write to. Defaults to "".
        text (str): string to append. Defaults to "".

    Returns:
        number of characters written
    """
    if filename:
        with open(filename, 'a', encoding='utf-8') as f:
            text = str(text)
            chars = f.write(text)
    return chars
