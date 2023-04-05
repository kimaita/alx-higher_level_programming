#!/usr/bin/python3
"""This module defines a class `LockedClass`
"""


class LockedClass:
    """This class has no attributes and will reject dynamic attributes
    except for `first_name`.
    """

    __slots__ = ['first_name']

    def __init__(self):
        pass
