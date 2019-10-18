#!/usr/bin/python3
""" This module creates a function that adds a new attribute to an object
if it’s possible
See:
    ./101-main.py test file
"""


def add_attribute(obj, name, value):
    """
    Add a new attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
