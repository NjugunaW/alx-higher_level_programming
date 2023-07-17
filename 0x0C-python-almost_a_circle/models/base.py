#!/usr/bin/python3

"""
A Class Base
"""
import os
import re
from random import randint
from json import JSONDecoder, JSONEncoder
from turtle import Pen

class Base:
    """
    This is the class that will be the base of all other classes in this project.
    The goal of this project is to manage attributes in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the class constructor
        Args:
            id (int): Integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

