#!/usr/bin/python3
""" This module returns the number of lines of a text file
See:
    ./1-main.py test file
"""


def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        num_lines = sum(1 for line in f)
        return (num_lines)
