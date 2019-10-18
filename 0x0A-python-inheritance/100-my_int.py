#!/usr/bin/python3
""" This module create a class MyInt that inherits from int:
See:
    ./100-main.py test file
"""


class MyInt(int):
    """
    MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """
        Returns the opposite of equal
        """
        if int(self) != int(other):
            return True
        else:
            return False

    def __ne__(self, other):
        """
        Returns the oppositeof not equal
        """
        if int(self) == int(other):
            return True
        else:
            return False
