#!/usr/bin/python3
""" This module create Class Rectangle that inherits from Base.
See:
    ./8-main.py test file
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation
        Args:
            id: is an integer
            width: width of a rectangle
            height: height of a rectangle
            x: vector x
            y: vector y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x property
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y property
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return Area
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle
        """
        for row in range(self.__y):
            print()
        for row in range(self.__height):
            for col in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args is not None and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])
        else:
            for arg, value in kwargs.items():
                setattr(self, arg, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of Rectangle
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for arg in range(len(attrs)):
            return {'id': getattr(self, attrs[0]),
                    'width': getattr(self, attrs[1]),
                    'height': getattr(self, attrs[2]),
                    'x': getattr(self, attrs[3]),
                    'y': getattr(self, attrs[4])}
