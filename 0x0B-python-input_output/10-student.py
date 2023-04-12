#!/usr/bin/python3
"""This module defines a class, Student """


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the object's dictionary representation"""
        if attrs and type(attrs) == list and (not any(type(attr) != str
                                                      for attr in attrs)):
            return {k: val for k, val in self.__dict__.items() if k in attrs}
        return self.__dict__
