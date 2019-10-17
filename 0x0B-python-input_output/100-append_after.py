#!/usr/bin/python3
""" This module inserts a line of text to a file,
after each line containing a specific string
See:
    ./100-main.py test file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append a new string
    """
    line = []
    with open(filename) as f:
        text = f.read()
        line = text.split("\n")
    for i in range(len(line)):
        if search_string in line[i]:
            line[i] = line[i] + "\n" + new_string
        elif len(line) - 1 != i:
            line[i] = line[i] + "\n"
    with open(filename, 'w') as f:
        f.write("".join(line))
