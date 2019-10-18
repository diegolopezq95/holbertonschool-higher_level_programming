#!/usr/bin/python3
""" This module write a function that reads a text file
See:
    ./0-main.py test file
"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
