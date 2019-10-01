#!/usr/bin/python3
""" This module creates an empty class Square that defines a square
Example:
    ./1-main.py test file
Private instance attribute:
    size
"""


class Square:
    """ Empty class Square now with size private attribute
    """
    def __init__(self, size):
        """
        Instantiation with size
        Args:
            size: size of the square
        """
        self.__size = size
