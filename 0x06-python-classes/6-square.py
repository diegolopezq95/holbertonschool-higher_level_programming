#!/usr/bin/python3
""" This module creates an empty class Square that defines a square
Example:
    ./3-main.py test file
Private instance attribute:
    size
"""


class Square:
    """ Empty class Square now with getters and setters
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiation with size and errors
        Args:
            size: size of the square and is positive.
            position: position of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Size getter. Returns the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size setter. Sets the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Position getter. Returns the position of thesquare
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Position setter. Sets the position of the square
        """
        if (isinstance(value, tuple) or len(value) == 2 or
            isinstance(value[0], int) or isinstance(value[1], int) or
           (value[0] >= 0 or value[1] >= 0)):
            self._position = value
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Print a Square depending of the size
        includes the position
        """
        if self.__size == 0:
            print()
        if self.__position:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
