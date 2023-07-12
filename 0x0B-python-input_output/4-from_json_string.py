#!/usr/bin/python3

"""
A module that returns an object
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    This module returns an object represented by a JSON string
    :my_str:
    :return:
    """
    return json.loads(my_str)
