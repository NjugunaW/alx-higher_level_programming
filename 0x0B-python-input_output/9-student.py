#!/usr/bin/python3
"""
A class Student that defines a student
"""


class Student:
    """
    A class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        This method is called to initalize variables instances
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
