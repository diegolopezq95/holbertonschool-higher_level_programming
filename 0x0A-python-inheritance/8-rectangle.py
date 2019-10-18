#!/usr/bin/python3
""" This module creates a class BaseGeometry and
a class Rectangle that inherits from BaseGeometry
See:
    ./8-main.py test file
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
