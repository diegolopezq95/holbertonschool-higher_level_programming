#!/usr/bin/python3
""" This module creates a class BaseGeometry
See:
    ./7-main.py test file
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
