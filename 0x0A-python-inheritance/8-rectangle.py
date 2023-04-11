#!/usr/bin/python3
"""This module contains a base geometry class and an inherited class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
