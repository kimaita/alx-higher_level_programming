#!/usr/bin/python3
"""This module defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle with its dimensions"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width attribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height attribute"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x attribute"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y attribute"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Calculates the Rectangle instance's area

        Returns:
            int: width * height
        """
        return self.height * self.width

    def display(self):
        """Prints a rectangle using `#` starting at given coordinates(x, y)
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' '*self.x+'#'*self.width)

    def __str__(self):
        """Return the Rectangle instance information"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -" \
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates an instance's attributes

        order of args: id, width, height, x, y
        """
        argc = len(args)

        if args and argc:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the Rectangle's dictionary representation
        """
        rect_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return rect_dict
