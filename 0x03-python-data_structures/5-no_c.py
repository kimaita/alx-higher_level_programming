#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string

    Args:
        my_string: string to replace occurences of c or C

    Returns:
        the new string
    """
    return ''.join([let if let.lower() != 'c' else '' for let in my_string])
