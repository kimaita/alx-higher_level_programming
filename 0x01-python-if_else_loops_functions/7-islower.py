#!/usr/bin/python3
def islower(c):
    """Returns if a character is lowercase or not"""
    if ord('a') <= ord(c) >= ord('z'):
        return True
    return False
