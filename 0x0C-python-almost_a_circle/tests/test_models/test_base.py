#!/usr/bin/python3

"""Unittest for class Base"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import os
from io import StringIO
import pep8

class TestBase(unittest.TestCase):
    """Tests for class Base"""
    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
        base1 = Base(12)
        self.assertEqual(base1.id, 12)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base("Hi")
        self.assertEqual(base.id, 'Hi') # should id be an int?

    def test_to_json_string(self):
        """Tests for func to_json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), type(
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'))

    def test_save_to_file(self):
        """Tests for save_to_file in class Base"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = Square(2, 4)
        b1 = Base(12)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1])
        file = open("Rectangle.json", "r")
        pyfile = json.loads(file)
        self.assertTrue(os.path.isfile('Rectangle.json'))
        self.assertTrue(os.path.isfile('Square.json'))
        self.assertEqual(

        def test_from_json_string(self):
            """Test for func from_json_string in class Base"""
            list_input = [{'id': 12, 'width': 3, 'height': 4},
                          {'id': 5, 'width': 6, 'height': 7}]

if __name__ == "__main__":
    unittest.main()