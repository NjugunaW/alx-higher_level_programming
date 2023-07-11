#!/usr/bin/python3

"""
This function contains a function that returns True if the object is an instance
of  a class that inherited (directly or indirectly) from specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class;
    otherwise False.
    :obj: The object in question
    :a_class: The class to be checked
    :return:  True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
