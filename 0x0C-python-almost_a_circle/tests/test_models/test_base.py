#!/usr/bin/python3
"""Unit tests for the `Base` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_init(self):
        """Test the initialization i.e. id assignment"""
        first = Base(23)
        self.assertEqual(first.id, 23)
        second = Base()
        self.assertEqual(second.id, 1)
        another = Base(3)
        self.assertEqual(another.id, 3)
        w_none = Base(None)
        self.assertEqual(w_none.id, 2)

    def test_to_json_string(self):
        """Test dict->JSON string serialization"""
        r1 = {'id': 89, 'width': 10, 'height': 4}
        r2 = {'id': 7, 'width': 1, 'height': 7}
        self.assertEqual(Base.to_json_string([r1, r2]),
                         '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]')

    def test_to_json_string_emptynone(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_save_to_file(self):
        """Test the dict list->JSON->file operation"""
        r1 = Rectangle(10, 7, 2, 8, 568)
        r2 = Rectangle(2, 4, 0, 2, 77)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            f_dict = file.read()
        self.assertEqual(f_dict,
                         '[{"id": 568, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 77, "width": 2, "height": 4, "x": 0, "y": 2}]')

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            f_dict = file.read()
        self.assertEqual(f_dict, '[]')
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            f_dict = file.read()
        self.assertEqual(f_dict, '[]')
