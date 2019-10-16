#!/usr/bin/python3
""" This module appends a string at the end of a text file
and returns the number of characters
See:
    ./4-main.py test file
"""


def append_write(filename="", text=""):
    with open(filename, 'a+', encoding='utf-8') as f:
        return f.write(text)
