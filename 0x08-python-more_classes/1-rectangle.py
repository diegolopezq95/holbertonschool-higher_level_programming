#!/usr/bin/python3
""" This module write a class Rectangle
See:
    ./1-main.py test file
"""


class Rectangle:
    """
    Class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation with size and errors
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("wigth must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
