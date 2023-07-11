#!/usr/bin/python3

"""
A module that returns the JSON rep of an object
"""
import json

def to_json_string(my_obj):
    """
    This module  returns the JSON representation of an object (string)
    """

    return json.dumps(my_obj)
