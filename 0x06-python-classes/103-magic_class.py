#!/usr/bin/python3
import math
""" This module is for a Magic Class
Private instance attribute:
    radius
"""


class MagicClass:
    """ Magic Class for bytecode
    """
    def __init__(self, radius=0):
        """
        Instantiation with size and errors
        Args:
            radius: radius of a circumference
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Return the area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Return circumference
        """
        return 2 * math.pi * self.__radius
