#!/usr/bin/python3
""" This module creates a class BaseGeometry and
a class Rectangle that inherits from BaseGeometry
See:
    ./9-main.py test file
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Create class Rectangle inherit from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area() method implemented
        """
        return (self.__width * self.__height)
        return (self.__width * self.__height)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
