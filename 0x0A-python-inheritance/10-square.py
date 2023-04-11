#!/usr/bin/python3
"""This module contains a base geometry class and some inherited classes"""


class BaseGeometry:
    """A class for input validation"""

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Checks if a given argument is an integer greater then 0

        Args:
            name (str): a name for the `value` argument
            value (int): the value to validate

        Raises:
            TypeError: when `value` is not an `int`
            ValueError: when `value` is not greater than 0
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """Describes a rectangle, with width and height
    """

    def __init__(self, width, height):
        """Initializes an instance, setting the width and height

        Args:
            width (int): rectangle's width
            height (height): rectangle's height
        """
        if super().integer_validator('width', width) is None:
            self.__width = width
        if super().integer_validator('height', height) is None:
            self.__height = height

    def area(self):
        """Calculates and returns the area of the object
        """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Describes a square
    """

    def __init__(self, size):
        """Initializes an instance with a given size

        Args:
            size (int): square's dimension
        """
        super().__init__(size, size)

    def area(self):
        return super().area()
