#!/usr/bin/python3
"""This module defines a single class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Describes a square
    """

    def __init__(self, size):
        """Initializes an instance with a given size

        Args:
            size (int): square's dimension
        """
        if self.integer_validator("size", size) is None:
            self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
