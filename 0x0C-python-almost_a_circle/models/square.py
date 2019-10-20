#!/usr/bin/python3
""" This module create class Square that inherits from Rectangle.
See:
    ./9-main.py test file
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation
        Args:
            id: is an integer
            size: size of a square
            x: vector x
            y: vector y
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string Square
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
