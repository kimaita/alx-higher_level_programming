#!/usr/bin/python3
"""This module defines a single class `Square`
"""


class Square:
    """Defines a square
    """

    def __init__(self, size):
        """sets the object's private size attribute on initialization

        Args:
            size: size of square object
        """
        self.__size = size
