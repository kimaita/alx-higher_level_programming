#!/usr/bin/python3
"""This module contains a single class `MagicClass`

The class is reverse-engineered fron given Python ByteCode
"""


class MagicClass:
    """Describes a circle with a radius
    """
    import math
    __radius = 0

    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return (self.__radius**2)*math.pi

    def circumference(self):
        return 2*math.pi*self.__radius
