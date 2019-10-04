#!/usr/bin/python3
"""
This module adds two numbers
See:
    ./0-main.py test file
"""


def add_integer(a, b=98):
    """
    Method that adds two numbers (a + b)
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return a + b
