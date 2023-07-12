#!/usr/bin/python3

"""
This module has a function that writes an Object to a text file
using a JSON Representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation
    :my_obj:
    :filename:
    :return:
    """
    with open(filename, mode="w", encoding="utf-8") as f_ile:
        json.dump(my_obj, f_ile)
