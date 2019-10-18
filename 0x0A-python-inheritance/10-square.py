#!/usr/bin/python3
""" This module creates a class Square inherit from a class
Rectangle that is inherits from BaseGeometry
See:
    ./10-main.py test file
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherit from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area() method implemented
        """
        return (self.__size * self.__size)
