#!/usr/bin/python3
"""
This module adds a new attribute to an object
if possible
"""

def add_attribute(obj, name, value):
    """
    That adds a new attribute to an object if it’s possible

    Args:
        obj (object): The object to set as attribute
        name (str): Name for the new attribute
        value (int): Value to new attribute
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, arg, value)
    else:
        raise TypeError("can't add new attribute")
