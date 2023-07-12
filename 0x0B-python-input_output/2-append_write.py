#!/usr/bin/python3

"""
This module has a function that appends a string at the end of a
text file
"""


def append_write(filename="", text=""):
    """
    This function appends a string at eh end of a text file
    :filename:
    :text:
    :return: The number of characters added
    """

    with open(filename, mode="a", encoding="utf") as f_ile:
        return f_ile.write(text)
