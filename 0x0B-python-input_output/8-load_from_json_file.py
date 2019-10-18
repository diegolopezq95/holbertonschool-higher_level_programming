#!/usr/bin/python3
""" This module creates an Object from a “JSON file”
See:
    ./8-main.py test file
"""


import json


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
