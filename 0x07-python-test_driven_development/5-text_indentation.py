#!/usr/bin/python3
"""
This module prints a text with 2 new lines after each of the characters .,?
See:
    ./5-main.py test file
"""


def text_indentation(text):
    """
    Method that splits text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n')
    text = text.replace('?', '?\n')
    text = text.replace(':', ':\n')
    new = []
    string = []
    for char in text:
        for string in text.split("\n"):
            string.strip()
            new.append(string.strip())
        print("\n\n".join(new), end="")
        break
