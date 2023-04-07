#!/usr/bin/python3
"""This module contains a function for printing reformatted text"""


def text_indentation(text):
    """Prints a text with 2 new lines after each `.` `?` and `:`

    Args:
        text (str): text to reformat and print
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text = text.strip()
    i = 0
    len_text = len(text)
    while i < len_text:
        s = text[i]
        if s in ('.', '?', ':'):
            print(s)
            print('')
            # check for `index out of range` when checking if followed by space
            if i < len_text-1 and text[i+1] == ' ':
                i += 1
        else:
            print(s, end='')
        i += 1
