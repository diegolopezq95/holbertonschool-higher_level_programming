#!/usr/bin/python3
""" This module create Class Base.
The “base” of all other classes in this project
See:
    ./17-main.py test file
"""


import json
import os
import csv


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
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        lists = []
        if json_string is None or len(json_string) == 0:
            return lists
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a file
        """
        filename = cls.__name__ + ".json"
        lists = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                elements = cls.from_json_string(f.read())
                for elem in elements:
                    lists.append(cls.create(**elem))
                return lists
        else:
            return lists

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        CSV string representation of list_objs to a file
        """
        filename = cls.__name__ + ".csv"
        lists = []
        with open(filename, 'w') as csv_f:
            writer = csv.writer(csv_f, delimiter=',')
            if list_objs is None:
                writer.writerow([])
            else:
                if cls.__name__ == "Rectangle":
                    lists = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Square":
                    lists = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csv_f, fieldnames=lists)
                for arg in list_objs:
                    writer.writerow(arg.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of instances from a file
        """
        filename = cls.__name__ + '.csv'
        lists = []
        my_list = []
        if os.path.exists(filename):
            with open(filename, 'r') as csv_f:
                if cls.__name__ == "Rectangle":
                    lists = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Square":
                    lists = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(csv_f, fieldnames=lists)
                for row in reader:
                    for keys, values in row.items():
                        row[keys] = int(values)
                    my_list.append(row)
                return [cls.create(**elem) for elem in my_list]
        else:
            return lists
