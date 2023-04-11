#!/usr/bin/python3
"""This module defines a single class"""


class BaseGeometry:
    """A class with unimplemented method and input validation"""

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
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
