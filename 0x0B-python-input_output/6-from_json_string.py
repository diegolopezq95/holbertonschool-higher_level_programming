#!/usr/bin/python3
""" This module returns an object (Python data structure)
represented by a JSON string
See:
    ./6-main.py test file
"""


import json


def from_json_string(my_str):
    return json.loads(my_str)
