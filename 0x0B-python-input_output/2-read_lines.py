#!/usr/bin/python3
""" This module reads n lines of a text file (UTF8) and prints it
See:
    ./2-main.py test file
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")
