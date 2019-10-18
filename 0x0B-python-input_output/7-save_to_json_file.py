#!/usr/bin/python3
""" This module writes an Object to a text file, using a JSON
See:
    ./7-main.py test file
"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
