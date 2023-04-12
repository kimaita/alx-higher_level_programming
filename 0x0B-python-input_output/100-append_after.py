#!/usr/bin/python3
"""This module contains a function for altering a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a given string

    Args:
        filename (str): name of file. Defaults to "".
        search_string (str): string to look for. Defaults to "".
        new_string (str): string to append. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line+new_string if search_string in line else line
                 for line in f.readlines()]

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
