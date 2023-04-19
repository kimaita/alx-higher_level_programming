#!/usr/bin/python3
"""Unit tests for the `Base` class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_init(self):
        """Test the initialization i.e. id assignment"""
        first = Base(23)
        self.assertEqual(first.id, 23)
        auto_1 = Base()
        self.assertEqual(auto_1.id, 1)
        auto_2 = Base()
        self.assertEqual(auto_2.id, 2)
        second = Base(67)
        self.assertEqual(second.id, 67)
        self.assertEqual(Base().id, 3)

    def test_to_json_string(self):
        """Test dict->JSON string serialization"""
        r1 = {'id': 89, 'width': 10, 'height': 4}
        r2 = {'id': 7, 'width': 1, 'height': 7}
        self.assertEqual(Base.to_json_string([r1, r2]),
                         '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]')

    def test_to_json_string_emptynone(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
