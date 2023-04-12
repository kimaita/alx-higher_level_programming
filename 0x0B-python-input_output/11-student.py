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
            return {k: val for k, val in vars(self).items() if k in attrs}
        return vars(self)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): dict with replacement values
        """
        for key in json:
            setattr(self, key, json[key])
