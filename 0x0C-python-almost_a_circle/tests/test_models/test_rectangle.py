#!/usr/bin/python3
"""Unit tests for the Rectangle class"""

import unittest
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
