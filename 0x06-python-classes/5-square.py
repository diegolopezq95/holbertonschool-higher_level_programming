#!/usr/bin/python3
""" This module creates an empty class Square that defines a square
Example:
    ./3-main.py test file
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

    def my_print(self):
        """
        Print a Square depending of the size
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
