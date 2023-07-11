#!/usr/bin/python3
"""
A class Student that defines jr student
"""


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        This method is called to initalize variable instances
        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): Age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrbts=None):
        """
        This function retrieves a dictionary representation of a Student instance
        """
        if attrbts is None:
            return self.__dict__
        new_dict = {}
        for jr in attrbts:
            try:
                new_dict[jr] = self.__dict__[jr]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """This function replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
