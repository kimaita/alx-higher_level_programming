#!/usr/bin/python3
"""This module defines a class `Rectangle`"""


class Rectangle:
    """Defines a rectangle given its dimensions"""

    def __init__(self, width=0, height=0):
        """Initializes a `Rectangle` instance setting its width and height

        Args
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """getter for the `height` attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the `height` attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """getter for the `width` attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the `width` attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
