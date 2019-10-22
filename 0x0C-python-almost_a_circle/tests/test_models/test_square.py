#!/usr/bin/python3
"""
Unittest for square.py
"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    All tests
    """
    def test_S(self):
        """
        Build Square test
        """
        s = Square(10, 2)
        self.assertEqual(5, s.id)
        self.assertEqual(10, s.size)
        self.assertEqual(2, s.x)
        self.assertEqual(0, s.y)

    def test_Area(self):
        """
        Square area test
        """
        s = Square(10, 2)
        self.assertEqual(100, s.area())

    def test_str(self):
        """
        Return str test
        """
        s = Square(5)
        self.assertEqual(s.__str__(), "[Square] (6) 0/0 - 5")
