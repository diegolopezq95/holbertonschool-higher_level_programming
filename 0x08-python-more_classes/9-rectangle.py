#!/usr/bin/python3
""" This module write a class Rectangle
See:
    ./9-main.py test file
"""


class Rectangle:
    """
    Class Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiation with size and errors
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string rectangle
        """
        string = []
        stringempty = ""
        if self.__width == 0 or self.__height == 0:
            return (stringempty)
        for row in range(self.__height):
            for col in range(self.__width):
                string.append(str(self.print_symbol))
            if row < self.__height - 1:
                string.append("\n")
        return("".join(string))

    def __repr__(self):
        """
        Returns a rectangle
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Delete instance of Rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Returns new Rectangle instance
        """
        return cls(size, size)
