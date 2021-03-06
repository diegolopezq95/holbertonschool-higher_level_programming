#!/usr/bin/python3
""" This module creates an empty class Square that defines a square
Example:
    ./102-main.py test file
Private instance attribute:
    size
"""


class Square:
    """ Empty class Square now with getters and setters
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

    @property
    def size(self):
        """
        Size getter. Returns the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size setter. Sets the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    Comparison methods
    """
    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ge__(self, other):
        return self.size >= other.size
