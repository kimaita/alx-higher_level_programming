#!/usr/bin/python3
"""This module contains a base class"""
import json


class Base:
    """This is the base class, managing the id attribute for all other classes

    Attributes:
        __nb_objects (int): keeps a count of created instances, to be used as a
        default id if not provided
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of
        Rectangle/Square object dictionaries

        Args:
            list_dictionaries (list): list of object dictionaries
        """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a Python list from a JSON string,
        with an empty list for `None` or empty strings

        Args:
            json_string (str): JSON string to deserialize
        """
        if not json_string:
            return []
        return json.loads(json_string) or []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects to a
        JSON file

        Args:
            list_objs (list): list of objects to serialize
        """
        filename = f'{cls.__name__}.json'
        dicts = [x.to_dictionary() for x in list_objs]
        json_dict = cls.to_json_string(dicts) if list_objs else '[]'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_dict)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of an inheriting class with given attributes
        """
        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 2)
        elif cls.__name__ == 'Square':
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """Reads in  and returns a list of objects from a JSON file"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()
                json_list = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in json_list]
        except FileNotFoundError:
            return []
