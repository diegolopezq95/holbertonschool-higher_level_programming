#!/usr/bin/python3
""" This module writes a string to the text and returns the num of characters
See:
    ./3-main.py test file
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
