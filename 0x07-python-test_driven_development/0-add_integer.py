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
    if a != a:
        return float("NaN")
    if b != b:
        return float("NaN")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if (a + b) == float("inf") or (a + b) == -float("inf"):
        return None
    return a + b
