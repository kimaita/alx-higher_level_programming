#!/usr/bin/python3
"""This module contains a single class `MagicClass`

The class is reverse-engineered from given Python ByteCode
"""


class MagicClass:
    """Describes a circle with a radius
    """
    import math

    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the circle's area."""
        return (self.__radius**2)*math.pi

    def circumference(self):
        """Calculates the circle's circumference."""
        return 2*math.pi*self.__radius
