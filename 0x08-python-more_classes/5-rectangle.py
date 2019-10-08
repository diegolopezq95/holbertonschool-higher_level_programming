#!/usr/bin/python3
""" This module write a class Rectangle
See:
    ./5-main.py test file
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
            raise ValueError("width must be >= 0")
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

    def area(self):
        """
        Area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string rectangle
        """
        string = []
        stringempty = ""
        if self.__width == 0 or self.__height == 0:
            return (stringempty)
        for row in range(self.__height):
            for col in range(self.__width):
                string.append("#")
            if row < self.__height - 1:
                string.append("\n")
        return("".join(string))

    def __repr__(self):
        """
        Returns a rectangle
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Delete instance of Rectangle
        """
        print("Bye rectangle...")
