#!/usr/bin/python3
""" This module checks if the object is exactly an instance of the class
See:
    ./2-main.py test file
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
