#!/usr/bin/python3
""" This module write a class Student
that defines a student by: (based on 12-student.py)
See:
    ./13-main.py test file
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        obj = {}
        if type(attrs) is list:
            for elem in attrs:
                if type(elem) == str and hasattr(self, elem):
                    obj[elem] = getattr(self, elem)
                else:
                    pass
        else:
            obj = self.__dict__
        return obj

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
