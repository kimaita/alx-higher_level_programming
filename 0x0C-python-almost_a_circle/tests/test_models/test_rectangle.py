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
        with self.assertRaises(TypeError):
            r1.width = '6'
            r1.height = '76'
            r1.x = {}
            r1.y = None
        with self.assertRaises(ValueError):
            r1.width = 0
            r1.height = -3
            r1.x = -3
            r1.y = -7

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

    def test_area(self):
        """Test the area() method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r1.width = 5
        self.assertEqual(r1.area(), 10)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_print):
        """Tests the display() method"""
        r1 = Rectangle(3, 3, 1, 2)
        r1.display()
        self.assertEqual('\n\n ###\n ###\n ###\n', mock_print.getvalue())

    def test_str(self):
        """Test the __str__() method"""
        r1 = Rectangle(4, 3, 2, 1, 34)
        self.assertEqual(r1.__str__(), '[Rectangle] (34) 2/1 - 4/3')
