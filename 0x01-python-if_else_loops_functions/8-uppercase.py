#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase."""
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            ch = chr(ord(ch) - 32)
        print('{}'.format(ch), end='')
    print()
