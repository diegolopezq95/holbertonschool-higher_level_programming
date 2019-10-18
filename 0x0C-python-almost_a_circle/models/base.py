#!/usr/bin/python3
""" This module create Class Base.
The “base” of all other classes in this project
See:
    ./0-main.py test file
"""

class Base:
    """
    Base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Instantiation
        Args:
            id: is an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
