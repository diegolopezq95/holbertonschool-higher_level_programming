#!/usr/bin/python3
""" This module creates a class MyList that inherits from list
See:
    ./1-main.py test file
"""


class MyList(list):
    """
    Class MyList prints sorted list
    """
    def print_sorted(self):
        print(sorted(self))
