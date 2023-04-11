#!/usr/bin/python3
"""This module defines a class for handling lists"""


class MyList(list):
    """Inherits from the list class and adds printing in sorted order
    functionality
    """

    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self.copy()))
