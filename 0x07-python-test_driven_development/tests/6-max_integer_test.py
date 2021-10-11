#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase)
    """
    Tests for max_integer()
    """"
    def max_integer(list=[]):
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([-1,-2,-3,-4]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer(['w','z', 'a', 'd']), 'z')
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1
