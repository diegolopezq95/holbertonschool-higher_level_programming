#!/usr/bin/python3
"""
Unittest for base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Base tests
    """
    def test_id(self):
        """
        Test no id
        """
        i = Base()
        self.assertEqual(1, i.id)

    def test_id_pos(self):
        """
        Test a positive id
        """
        i = Base(89)
        self.assertEqual(89, i.id)

    def test_id_neg(self):
        """
        Test a negative id
        """
        i = Base(-89)
        self.assertEqual(-89, i.id)

