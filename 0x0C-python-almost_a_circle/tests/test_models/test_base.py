#!/usr/bin/python3
"""Unit tests for the `Base` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    def test_init(self):
        """Test the initialization i.e. id assignment"""
        first = Base(23)
        self.assertEqual(first.id, 23)

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

    def test_from_json_string(self):
        """Tests the `from_json_string()` method"""
        json_str = '[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]'
        list_objs = Rectangle.from_json_string(json_str)
        self.assertListEqual(list_objs,
                             [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])

    def test_from_json_string_emptynone(self):
        list_objs = Rectangle.from_json_string('')
        self.assertListEqual(list_objs, [])
        list_objs = Rectangle.from_json_string(None)
        self.assertListEqual(list_objs, [])

    def test_create(self):
        """Tests the create() method"""
        rect_dict = {'height': 4, 'width': 10, 'id': 99}
        r1 = Rectangle.create(**rect_dict)
        self.assertTupleEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                              (99, 10, 4, 0, 0))
        sq_dict = {'size': 5, 'x': 2, 'y': 3, 'id': 456}
        s1 = Square.create(**sq_dict)
        self.assertTupleEqual((s1.id, s1.size, s1.x, s1.y),
                              (456, 5, 2, 3))

    def test_load_from_file(self):
        """Tests the `load_from_file() method"""
        r1 = Rectangle(10, 7, 2, 8, 211)
        Rectangle.save_to_file([r1])

        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(loaded_rectangles[0].__str__(),
                         '[Rectangle] (211) 2/8 - 10/7')

        s1 = Square(8, 2, 2, 678)
        Square.save_to_file([s1])
        loaded_squares = Square.load_from_file()
        self.assertEqual(loaded_squares[0].__str__(),
                         '[Square] (678) 2/2 - 8')
