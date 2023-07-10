#!/usr/bin/python3

def add_attribute(obj, arg, value):
    """
    That adds a new attribute to an object if it’s possible

    Args:
        obj (object): The object to set as attribute
        arg (str): Name for the new attribute
        value (int): Value to new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, arg, value)
    else:
        raise TypeError("can't add new attribute")
