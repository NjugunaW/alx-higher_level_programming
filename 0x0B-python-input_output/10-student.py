#!/usr/bin/python3
"""
A Student that defines a student
"""


class Student:
    """
    A class Student that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """This method is called to initialize variable  instances

        Attributes:
                  first_name (str): The first name of the student.
                  last_name (str): The last name of the student.
                  age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrbts=None):
        """
        Retrieves a dictionary representation of the Student instance.
        
        Attributes:
                  attrbts (list): Attributes
        """

        if (type(attrbts) == list and
                all(type(ab) == str for ab in attrbts)):
            return {k: getattr(self, k) for k in attrbts if hasattr(self, k)}
        return self.__dict__
