#!/usr/bin/python3
"""Unit tests for the Rectangle class"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defines tests for the Rectangle class
    """

    def test_init_wh(self):
        """Test the class instance initialization"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_init_wh_xy(self):
        """Test the class instance initialization"""
        r1 = Rectangle(10, 2, 2, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)

    def test_init_wh_xy_id(self):
        """Test the class instance initialization"""
        r1 = Rectangle(10, 2, 2, 3, 45)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 45)

    def test_badinit_width(self):
        with self.assertRaises(TypeError, msg='width must be an integer'):
            Rectangle("1", 2)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            Rectangle(0, 2)
            Rectangle(-3, 2)

    def test_badinit_height(self):
        with self.assertRaises(TypeError, msg='height must be an integer'):
            Rectangle(2, "2")
        with self.assertRaises(ValueError, msg='height must be > 0'):
            Rectangle(2, -2)
            Rectangle(2, 0)

    def test_badinit_x(self):
        with self.assertRaises(TypeError, msg='x must be an integer'):
            Rectangle(2, 2, '0', 0)
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            Rectangle(2, 2, -5, 0)

    def test_badinit_y(self):
        with self.assertRaises(TypeError, msg='y must be an integer'):
            Rectangle(2, 2, 0, '0')
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            Rectangle(2, 2, 0, -2)

    def test_area(self):
        """Test the area() method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r1.width = 5
        self.assertEqual(r1.area(), 10)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_orig(self, mock_print):
        """Tests the display() method"""
        r1 = Rectangle(3, 3)
        r1.display()
        self.assertEqual('###\n###\n###\n', mock_print.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_xy(self, mock_print):
        """Tests the display() method"""
        r1 = Rectangle(3, 3, 1, 2)
        r1.display()
        self.assertEqual('\n\n ###\n ###\n ###\n', mock_print.getvalue())

    def test_str(self):
        """Test the __str__() method"""
        r1 = Rectangle(4, 3, 2, 1, 34)
        self.assertEqual(r1.__str__(), '[Rectangle] (34) 2/1 - 4/3')

    def test_update_args(self):
        """Tests the update() method using only *args"""
        r1 = Rectangle(2, 5, 1, 1, 67)
        r1.update(67)
        self.assertEqual(r1.id, 67)
        r1.update(67, 12)
        self.assertEqual(r1.width, 12)
        r1.update(67, 12, 6)
        self.assertEqual(r1.height, 6)
        r1.update(67, 12, 6, 3)
        self.assertEqual(r1.x, 3)
        r1.update(67, 12, 6, 3, 4)
        self.assertEqual(r1.y, 4)

    def test_update_badargs(self):
        r1 = Rectangle(2, 3, 4, 4, 23)
        with self.assertRaises(TypeError):
            r1.update(2, '45')
            r1.update(2, 45, '30')
            r1.update(2, 45, 30, '1')
        with self.assertRaises(ValueError):
            r1.update(34, 0, 0)
            r1.update(34, 4, 5, -1)

    def test_update_kwargs(self):
        """Test the update() method using only **kwargs"""
        r1 = Rectangle(20, 30)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertTupleEqual((r1.width, r1.x), (1, 2))
        r1.update(x=1, height=2, y=3, width=4, id=89)
        self.assertTupleEqual(
            (r1.width, r1.height, r1.x, r1.y, r1.id), (4, 2, 1, 3, 89))

    def test_update_badkwargs(self):
        r1 = Rectangle(20, 30)
        with self.assertRaises(TypeError, msg='height must be an integer'):
            r1.update(height='1')
        with self.assertRaises(ValueError, msg='width must be > 0'):
            r1.update(width=0)
        with self.assertRaises(TypeError, msg='x must be an integer'):
            r1.update(x='4')
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            r1.update(y=-3)

    def test_args_kwargs(self):
        """Tests a combination of both args and kwargs

        **kwargs skipped if *args exists and is not empty
        """
        r1 = Rectangle(3, 4)
        r1.update(999, height=7)
        self.assertTupleEqual((r1.id, r1.height), (999, 4))
        r1.update(height=7)
        self.assertTupleEqual((r1.id, r1.height), (999, 7))

    def test_to_dictionary(self):
        """Tests the to_dictionary() method"""
        r1 = Rectangle(10, 2, 1, 9, 128)
        self.assertDictEqual(
            r1.to_dictionary(), {'x': 1, 'y': 9, 'id': 128, 'height': 2, 'width': 10})

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

    def test_save_to_file_empty(self):
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

    def test_load_from_file(self):
        """Tests the `load_from_file() method"""
        r1 = Rectangle(10, 7, 2, 8, 211)
        Rectangle.save_to_file([r1])

        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(loaded_rectangles[0].__str__(),
                         '[Rectangle] (211) 2/8 - 10/7')

    def test_create(self):
        """Tests the create() method"""
        rect_dict = {'height': 4, 'width': 10, 'id': 99}
        r1 = Rectangle.create(**rect_dict)
        self.assertTupleEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                              (99, 10, 4, 0, 0))
