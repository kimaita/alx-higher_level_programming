#!/usr/bin/python3
"""This module contains a single function for printing a name introduction
"""


def say_my_name(first_name, last_name=""):
    """Prints a name introduction given two names.

    The introduction is "My name is <first name> <last name>"

    Args:
        first_name (str): the first name
        last_name (str, optional): the last name. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
