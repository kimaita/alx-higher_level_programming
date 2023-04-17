#!/usr/bin/python3
""""""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from the Rectangle but has same width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the Square's dimensions"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the square's dimensions

        Args:
            value (int): Squares's length
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the Square instance information"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the instance attributes"""
        if args and len(args):
            attrs = ['id', 'size', 'x', 'y']
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the Square's dictionary representation
        """
        rect_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return rect_dict
