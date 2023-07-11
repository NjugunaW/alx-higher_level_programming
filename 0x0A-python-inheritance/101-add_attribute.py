#!/usr/bin/python3

"""
This module contains a function that adds a new attribute
"""


def add_attribute(obj, name, value):
    """
    This function adds a new attribute to a class when possible
    :obj (object): The object to set as attribute
    :name (str): Name for the new attribute
    :value (int): Value to new attribute
    :return:
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
