#!/usr/bin/python3
"""
A function that retursn True if object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """
    This function returns True if object is similar to specified class
    
    Args: 
        (obj:): the object being checked
        (a_class:): the class
    """

    return type(obj) == a_class
