#!/usr/bin/python3
"""This module defines a single class `Square`
"""


class Square:
    """Defines a square
    """

    def __init__(self, size=0):
        """sets the object's private size attribute on initialization

        Args:
            size (int): size of square object
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return the current square area
        """
        return (self.__size**2)

    def size(self):
        """getter for the square's `__size` attribute
        """
        return self.__size

    def size(self, value):
        """setter for the square's `__size` attribute

        Args:
            value (int): value to set `__size` to
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
