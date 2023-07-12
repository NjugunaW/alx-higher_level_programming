#!/usr/bin/python3

"""
This function writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file
    :filename:
    :text:
    :return: the number of characters written
    """
    with open(filename, mode="w", encoding="utf") as f_ile:
        return f_ile.write(text)
