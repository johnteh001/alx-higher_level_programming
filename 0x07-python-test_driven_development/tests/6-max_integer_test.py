#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger Tests for maximum integer in argument."""

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([12, 8, 7, 2]), 12)
        self.assertEqual(max_integer([2, 5, 27, 3, 5]), 27)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -7, -4, -2]), -1)
        self.assertEqual(max_integer([-8, -8, -9, 1]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([3]), 3)
