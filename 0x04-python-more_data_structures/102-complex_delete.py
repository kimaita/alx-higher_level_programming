#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: the dictionary
        value: value to delete keys
    """
    init_len = len(a_dictionary)
    keys = list(a_dictionary.keys())
    i = 0
    while i < init_len:
        k = keys[i]
        if a_dictionary.get(k) == value:
            del a_dictionary[k]
        i += 1
    return a_dictionary
