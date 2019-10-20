#!/usr/bin/python3
""" This module create Class Base.
The “base” of all other classes in this project
See:
    ./14-main.py test file
"""


import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation
        Args:
            id: is an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        lists = []
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string(lists))
            else:
                for arg in list_objs:
                    lists.append(arg.to_dictionary())
                f.write(cls.to_json_string(lists))
