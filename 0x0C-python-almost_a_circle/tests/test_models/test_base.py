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

    def test_string_input(self):
        """
        Test a string id
        """
        i = Base("Holberton")
        self.assertEqual("Holberton", i.id)


    def test_docs_B(self):
        """
        Test for Base class docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_docs_R(self):
        """
        Test for Rectabgle class docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_docs_S(self):
        """
        Test for Square class docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_to_json_none(self):
        """
        Test for to json string empty list
        """
        i = Base.to_json_string(None)
        self.assertEqual("[]", i)

    def test_to_json_string(self):
        """
        Test for to json string with args
        """
        i = Base.to_json_string([{"John": 23}, {"Betty": 56}])
        self.assertEqual(str, type(i))

    def test_save_to_file_none(self):
        """
        Tests save to file None
        """
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")
