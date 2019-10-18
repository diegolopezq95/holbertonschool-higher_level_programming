#!/usr/bin/python3
""" This module returns the JSON representation of an object (string)
See:
    ./5-main.py test file
"""


import json


def to_json_string(my_obj):
    return json.dumps(my_obj, sort_keys=True)
