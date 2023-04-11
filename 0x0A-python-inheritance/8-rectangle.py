#!/usr/bin/python3
""""""


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
    """_summary_


    """
    __width = int()
    __height = int()

    def __init__(self, width, height):
        if self.integer_validator('width', width):
            self.__width = width
        if self.integer_validator('height', height):
            self.__height = height
