#!/usr/bin/python3


"""
This module has a class Student that defines a Student
"""


class Student:
    """
    The Class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        This function is called to initalize variable instances
        :first_name:
        :last_name:
        :age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function retrieves a dictionary representation
        of a Student instance
        :attrs:
        :return:
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for jr in attrs:
            try:
                new_dict[jr] = self.__dict__[jr]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """
        This function replaces all attributes of the Student instance
        :json:
        :return:
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
