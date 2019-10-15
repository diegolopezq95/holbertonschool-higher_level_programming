#!/usr/bin/python3
""" This module creates a class BaseGeometry and
a class Rectangle that inherits from BaseGeometry
See:
    ./9-main.py test file
"""


class BaseGeometry:
    """
    Adding integers validator method
    """
    def area(self):
        """
        Nothing happens
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
