#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    returns True if object is similar to specified class
    """
    if type(obj) == a_class:
        return True

    return False
