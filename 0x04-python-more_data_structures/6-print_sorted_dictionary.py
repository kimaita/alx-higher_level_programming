#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.
    Keys are sorted by alphabetical order

    Args:
        a_dictionary: the dctionary
    """
    sorted_keys = sorted(a_dictionary.keys())
    for k in sorted_keys:
        print(f"{k}: {a_dictionary.get(k)}")
