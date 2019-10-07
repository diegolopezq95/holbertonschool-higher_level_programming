#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """clas for test """
    def test_max_last(self):
        """ test 1 """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_first(self):
        """ test 2"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_float(self):
        """ test 3 """
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 5.6]), 5.6)

    def test_empty_list(self):
        """ test 4 """
        self.assertEqual(max_integer([]), None)

    def test_max_positive(self):
        """ test 5 """
        self.assertEqual(max_integer([2, -1, -3]), 2)

    def test_max_one(self):
        """ test 6 """
        self.assertEqual(max_integer([1024]), 1024)

    def test_max_negative(self):
        """ test 7 """
        self.assertEqual(max_integer([-1024, -1025]), -1024)

    def test_string_list(self):
        """ test 8 """
        with self.assertRaises(TypeError):
            max_integer(["Holberton", 1, 2, 3, "4"])

    def test_tuple_list(self):
        """ test 9 """
        with self.assertRaises(TypeError):
            max_integer([1, (2, 3), (3, 5), 6])

    def test_dict_list(self):
        """ test 10 """
        with self.assertRaises(KeyError):
            max_integer({"Johnnie Waler": 100, "Jack Daniel's": 101})

    def test_none_list(self):
        """ test 11 """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_num_list(self):
        """ test 12 """
        with self.assertRaises(TypeError):
            max_integer(1024)

    def test_max_last(self):
        """ test 13 """
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

if __name__ == '__main__':
    unittest.main()
