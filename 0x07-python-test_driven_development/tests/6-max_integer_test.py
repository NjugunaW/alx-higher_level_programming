#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
 """
 Class that tests a max int function
 """

    def test_max_integer(self):
        """
        This tests tha max integer in a list with positive and negative numbers
        """
        self.assertEqual(max_integer([2, 7, 9, 6]), 9)
        self.assertEqual(max_integer([-2, -7, -9, -6]), -2)
        self.assertEqual(max_integer([2.2, 7.3, 9.7, 6.9]), 9.7)
        self.assertEqual(max_integer([5, 0]), 5)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([20000000, 100000000]), 100000000)

    def test_wrong_types(self):
        """
        Tests the max int in a list with wrong parameter types
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Wow", 2, "Hello" 3, "There"])
