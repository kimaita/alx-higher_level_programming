#!/usr/bin/python3
"""Unit tests for the `Square` class"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    """Defines tests for the Square class
    """

    def test_init(self):
        """Tests the init method"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_badinit(self):
        with self.assertRaises(TypeError, msg='width must be an integer'):
            Square('5')
        with self.assertRaises(ValueError, msg='width must be > 0'):
            Square(0)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            Square(-5)
        with self.assertRaises(TypeError, msg='x must be an integer'):
            Square(5, '1')
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            Square(5, -1)
        with self.assertRaises(TypeError, msg='y must be an integer'):
            Square(5, 1, '1')
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            Square(5, 1, -1)

    def test_str(self):
        """Test the __str__() method"""
        s1 = Square(5, 2, 4, 56)
        self.assertEqual(s1.__str__(), '[Square] (56) 2/4 - 5')

    def test_size(self):
        """Tests the size getter and setter"""
        s1 = Square(10)
        s1.size = 7
        self.assertEqual(s1.size, 7)
        s1.size = 34
        self.assertEqual(s1.size, 34)

    def test_badsize(self):
        """Tests the size getter and setter"""
        s1 = Square(10)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            s1.size = '7'
        with self.assertRaises(ValueError, msg='width must be > 0'):
            s1.size = -3

    def test_area(self):
        """Tests the area() method"""
        s1 = Square(7)
        self.assertEqual(s1.area(), 49)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_orig(self, mock_print):
        """Tests the display() method"""
        s1 = Square(3)
        s1.display()
        self.assertEqual('###\n###\n###\n', mock_print.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_xy(self, mock_print):
        """Tests the display() method"""
        s1 = Square(3, 1, 2)
        s1.display()
        self.assertEqual('\n\n ###\n ###\n ###\n', mock_print.getvalue())

    def test_update_args(self):
        """Tests the update method with args only"""
        s1 = Square(3)
        s1.update(45, 6)
        self.assertTupleEqual((s1.id, s1.size), (45, 6))
        s1.update(45, 6, 3, 3)
        self.assertTupleEqual((s1.id, s1.size, s1.x, s1.y), (45, 6, 3, 3))

    def test_update_badargs(self):
        s1 = Square(3)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.update(23, '56')
        with self.assertRaises(ValueError, msg="width must be >= 0"):
            s1.update(23, -56)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            s1.update(23, 6, '5')
        with self.assertRaises(ValueError, msg="y must be > 0"):
            s1.update(23, 6, 3, -2)

    def test_update_kwargs(self):
        """Test the update() method using only **kwargs"""
        s1 = Square(20)
        s1.update(size=1)
        self.assertEqual(s1.size, 1)
        s1.update(size=1, x=2)
        self.assertTupleEqual((s1.size, s1.x), (1, 2))
        s1.update(x=1, y=3, size=4, id=89)
        self.assertTupleEqual(
            (s1.size, s1.x, s1.y, s1.id), (4, 1, 3, 89))

    def test_update_badkwargs(self):
        """Test the update() method using only **kwargs"""
        s1 = Square(20)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            s1.update(size='1')
        with self.assertRaises(TypeError, msg='x must be an integer'):
            s1.update(x='1')
        with self.assertRaises(ValueError, msg='width must be > 0'):
            s1.update(size=0)
        with self.assertRaises(ValueError, msg='x must be >='):
            s1.update(x=-2)

    def test_args_kwargs(self):
        """Tests a combination of both args and kwargs

        **kwargs skipped if *args exists and is not empty
        """
        s = Square(3, 4, 5)
        s.update(999, size=7)
        self.assertTupleEqual((s.id, s.size), (999, 3))
        s.update(size=7)
        self.assertEqual(s.size, 7)

    def test_to_dictionary(self):
        """Tests the to_dictionary() method"""
        s = Square(5, 2, 2, 678)
        self.assertDictEqual(s.to_dictionary(),
                             {'id': 678, 'x': 2, 'size': 5, 'y': 2})

    def test_load_from_file(self):
        """Tests the `load_from_file() method"""
        s1 = Square(8, 2, 2, 678)
        Square.save_to_file([s1])
        loaded_squares = Square.load_from_file()
        self.assertEqual(loaded_squares[0].__str__(),
                         '[Square] (678) 2/2 - 8')

    def test_save_to_file(self):
        """Test the dict list->JSON->file operation"""
        s1 = Square(10, 2, 2, 87)
        s2 = Square(4, 0, 0, 77)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            f_dict = file.read()
        self.assertEqual(f_dict,
                         '[{"id": 87, "size": 10, "x": 2, "y": 2}, {"id": 77, "size": 4, "x": 0, "y": 0}]')

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            f_dict = file.read()
        self.assertEqual(f_dict, '[]')

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            f_dict = file.read()
        self.assertEqual(f_dict, '[]')

    def test_create(self):
        """Tests the create() method"""
        sq_dict = {'size': 5, 'x': 2, 'y': 3, 'id': 456}
        s1 = Square.create(**sq_dict)
        self.assertTupleEqual((s1.id, s1.size, s1.x, s1.y),
                              (456, 5, 2, 3))
