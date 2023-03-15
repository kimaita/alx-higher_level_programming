#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    Args:
        a_dictionary: the dictionary to remove the key
        key: the key to remove. Defaults to "".

    Returns:
        the modified dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
