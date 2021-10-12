"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer"""

    def testMax(self):
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)

    def testNeg(self):
        self.assertEqual(max_integer([-1,-2,-3,-4]), -1)

    def testAlpha(self):
        self.assertEqual(max_integer(['w','z', 'a', 'd']), 'z')

     def test_type(self):
        self.assertRaises(TypeError, max_integer((1, 2)))

if __name__ == '__main__':
    unittest.main()
