#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary:the dictionary to update
        key: a key for the value
        value: the value

    Returns:
        the updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
