#!/usr/bin/python3
"""This module defines a class `Rectangle` that represents a rectangle"""


class Rectangle:
    """Defines a rectangle given its dimensions

    There's methods for obtaining the area and perimeter
    """

    def __init__(self, width=0, height=0):
        """Initializes a `Rectangle` instance setting its width and height

        Attr:
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

    def area(self):
        """Calculates the rectangle's area"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the rectangle's perimeter"""
        if self.width and self.height:
            return 2*(self.width + self.height)
        return 0

    def __str__(self):
        """Return a string representation of the rectangle

        The rectangle is drawn using `#`
        """
        rect = ''
        if self.width and self.height:
            for i in range(self.height-1):
                rect += '#'*self.width+'\n'
            rect += '#'*self.width

        return rect

    def __repr__(self):
        """Returns a string representation of the rectangle
        sufficient to recreate a new instance"""
        return f'Rectangle({self.width}, {self.height})'
