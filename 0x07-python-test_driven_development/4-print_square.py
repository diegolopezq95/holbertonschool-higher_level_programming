#!/usr/bin/python3
"""
This module prints a square with the character #.
See:
    ./4-main.py test file
"""


def print_square(size):
    """
    Method that prints a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
