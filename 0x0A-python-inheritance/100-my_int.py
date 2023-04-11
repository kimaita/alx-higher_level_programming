#!/usr/bin/python3
"""This module defines an altered integer class"""


class MyInt(int):
    """Regular `int` class but with inverted equality operators"""

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
