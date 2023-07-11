#!/usr/bin/python3
"""
This function returns True if object is an instance of,
or if the object is an instance of a class that inherited from, 
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if object
    is an instance of,or if the object is an 
    instance of a class that inherited from, the specified class;
    otherwise False

    Args:
        obj (any): The object to be checked
        a_class (type): The class to check from
    """


    return isinstance(obj, a_class)
