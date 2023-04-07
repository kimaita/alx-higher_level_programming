#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Contains test cases for the function `max_integer`
    """

    def test_no_argument(self):
        """Defaults to an empty list and returns None"""
        self.assertEqual(max_integer(), None)

    def test_okay_args(self):
        """Should return the largest number"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([23, 2, 5, 4]), 23)
        self.assertEqual(max_integer([1, -23, 2, 5, 4]), 5)
        self.assertEqual(max_integer([-2, -5, -65, -15]), -2)
        self.assertEqual(max_integer([4]), 4)

    def test_not_iterable_or_all_ints(self):
        """Should raise a type error"""
        with self.assertRaises(TypeError):
            max_integer(23)
            max_integer([2, 3, {}])
            max_integer({})
