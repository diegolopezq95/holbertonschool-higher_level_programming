#!/usr/bin/python3
""" This module checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
See:
    ./4-main.py test file
"""


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)