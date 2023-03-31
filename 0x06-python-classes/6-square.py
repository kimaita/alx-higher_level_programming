#!/usr/bin/python3
"""This module defines a single class `Square`
"""


class Square:
    """Defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """sets the object's private `size` and `position` attributes
        on initialization

        Args:
            `size` (int): size of square object
            `position` (tuple): pair of coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for the square's `__size` attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for the square's `__size` attribute

        Args:
            `value` (int): value to set `__size` to
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """getter for the `__position` attribute

        Returns:
            __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter for `__position` attribute

        Args:
            value: tuple to set `__position` to

        Raises:
            TypeError: if `value` is not a tuple of 2 positive integers
        """
        if ((not isinstance(value, tuple)) or
            len(value) != 2 or
            (not isinstance(value[0], int)) or
            (not isinstance(value[1], int)) or
                value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Return the current square area
        """
        return (self.__size**2)

    def my_print(self):
        """Prints in `stdout` the square with the character `#`
        starting at `__position`
        """
        if self.size:
            for i in range(self.position[1]):
                print('')
            for i in range(self.size):
                print(' '*self.position[0], end='')
                print('#'*self.size, end='')
                print('')
        else:
            print('')
