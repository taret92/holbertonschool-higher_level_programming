#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_module_max_integer(self):
        """Test"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 1024, 25]), 1024)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


    def test_max_string(self):
        self.assertEqual(max_integer(["5", "7", "9"]), "9")
        self.assertEqual(max_integer(["Hello", "Good", "Bye"]), "Hello")
        self.assertEqual(max_integer("5"), "5")
        self.assertEqual(max_integer("4567"), "7")
        self.assertEqual(max_integer("abcxyz"), "z")
        self.assertEqual(max_integer(["a", "b", "c", "d", "e", "y", "z"]), "z")
        self.assertEqual(max_integer(["abc", "y"]), "y")


    def test_list_floats(self):
        self.assertEqual(max_integer([[1, 2], [2, 3]]), [2, 3])
        self.assertEqual(max_integer([{1, 2}, {2}, {3, 4}]), {1, 2})
        self.assertEqual(max_integer([-6.1, -9.8, -2.5, -3.7]), -2.5)
