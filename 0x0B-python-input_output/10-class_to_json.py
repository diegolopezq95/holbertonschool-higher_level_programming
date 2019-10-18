#!/usr/bin/python3
""" This module returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
See:
    ./10-main.py test file
"""


def class_to_json(obj):
    return getattr(obj, "__dict__")
