#!/usr/bin/python3
"""This module defines a class `Rectangle` that represents a rectangle"""


class Rectangle:
    """Defines a rectangle given its dimensions

    There's methods for obtaining the area and perimeter

    Attributes:
        number_of_instances (int): counter for created `Rectangle` instances
        print_symbol (Any): Used as symbol for string representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a `Rectangle` instance setting its width and height

        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        The rectangle is drawn using `print_symbol`
        """
        rect = ''
        if self.width and self.height:
            for i in range(self.height-1):
                rect += str(self.print_symbol)*self.width+'\n'
            rect += str(self.print_symbol)*self.width

        return rect

    def __repr__(self):
        """Returns a string representation of the rectangle
        sufficient to recreate a new instance"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Deletes an instance of `Rectangle`"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on their area, returning the larger

        Args:
            rect_1 (Rectangle): the first `Rectangle` object
            rect_2 (Rectangle): the second `Rectangle` object

        Returns:
            the larger `Rectangle` object or
            `rect_1` if both have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle with its dimensions set to `size`

        Args:
            size (int, optional): Value to set width and height to.
            Defaults to 0.
        """
        return Rectangle(size, size)
