#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiplies all values of a dictionary by 2

    Args:
        a_dictionary: the dictionary

    Returns:
        a new dictionary with all values multiplied by 2
    """
    new_dict = dict(map(lambda x: (x[0], x[1]*2), a_dictionary.items()))
    return new_dict
