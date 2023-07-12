#!/usr/bin/python3

"""
This module has a function that returns a dictionary
description with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    This function returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    :obj:
    :return:
    """
    return obj.__dict__
