#!/usr/bin/python3
"""This module contains a base geometry class and an inherited class"""


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
        if value.__class__ != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """Describes a rectangle, with width and height
    """
    __width = int()
    __height = int()

    def __init__(self, width, height):
        """Initializes an instance, setting the width and height

        Args:
            width (int): rectangle's width
            height (height): rectangle's height
        """
        if self.integer_validator('width', width):
            __width = width
        if self.integer_validator('height', height):
            __height = height
