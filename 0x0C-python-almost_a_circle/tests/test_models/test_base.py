#!/usr/bin/python3
"""Unit tests for the `Base` class"""
import unittest
from models.base import Base


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
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
