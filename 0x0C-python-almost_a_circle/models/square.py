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
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        size setter
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args is not None and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])
        else:
            for arg, value in kwargs.items():
                setattr(self, arg, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of Square
        """
        attrs = ['id', 'size', 'x', 'y']
        for arg in range(len(attrs)):
            return {'id': getattr(self, attrs[0]),
                    'size': getattr(self, attrs[1]),
                    'x': getattr(self, attrs[2]),
                    'y': getattr(self, attrs[3])}
