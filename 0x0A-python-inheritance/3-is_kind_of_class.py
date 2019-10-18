#!/usr/bin/python3
""" This module checks if the object is an instance or if the object is
an instance of a class that inherited from the specified class
See:
    ./3-main.py test file
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
