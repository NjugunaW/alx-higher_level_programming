#!/usr/bin/python3
"""This function returns True if
the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object
    is an instance of a class that inherited 
    (directly or indirectly) from the specified class;
    otherwise False.
    :obj: The object
    :a_class: The class
    :return: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
