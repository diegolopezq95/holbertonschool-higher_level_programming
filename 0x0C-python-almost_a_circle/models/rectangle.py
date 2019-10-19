#!/usr/bin/python3
""" This module create Class Rectangle that inherits from Base.
See:
    ./7-main.py test file
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
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @height.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @height.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

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
        if args is not None and len(args) is not 0:
            attrs = ["id", "width", "height", "x", "y"]
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])
        else:
            for arg, value in kwargs.items():
                setattr(self, arg, value)
