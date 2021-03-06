#!/usr/bin/python3
""" This module creates an empty class Square that defines a square
Example:
    ./3-main.py test file
Private instance attribute:
    size
"""


class Square:
    """ Empty class Square now with Area
    """
    def __init__(self, size=0):
        """
        Instantiation with size and errors
        Args:
            size: size of the square and is positive
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size * self.__size)
