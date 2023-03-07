#!/usr/bin/python3
def remove_char_at(str, n):
    """Removes the character at index n of str"""
    str_copy = []
    if (n < 0) or (n >= len(str)):
        return str
    for i in range(len(str)):
        str_copy.append('') if i == n else str_copy.append(str[i])
    return ''.join(str_copy)
