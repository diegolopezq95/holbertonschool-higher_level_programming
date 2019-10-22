#!/usr/bin/python3
"""
Unittest for rectangle.py
"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """
    All tests
    """
    def test_R(self):
        """
        Build rectangle test
        """
        r = Rectangle(10, 2)
        self.assertEqual(3, r.id)
        self.assertEqual(10, r.width)
        self.assertEqual(2, r.height)
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

    def test_Area(self):
        """
        Rectangle area test
        """
        r = Rectangle(10, 2)
        self.assertEqual(20, r.area())

    def test_str(self):
        """
        Return str test
        """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")
