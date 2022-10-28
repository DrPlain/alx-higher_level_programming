#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """contains test cases for the function max_integer()"""

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 3, 4, 6, 7, 8]), 8)

    def test_one_element_list(self):
        """List with one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_list_negative_int(self):
        """List of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_negative_positive_int(self):
        """List of positive and negative integers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_empty_list(self):
        """An empty list"""
        self.assertEqual(max_integer([]), None)

    def test_integer_and_float(self):
        """List of integer and float"""
        ints_and_float = [1.35, 5, 6.78, 15.55, 14]
        self.assertEqual(max_integer(ints_and_float), 15.55)

    def test_list_of_strings(self):
        """List of strings"""
        self.assertEqual(max_integer("gideon"), "o")


if __name__ == "__main__":
    unittest.main()
