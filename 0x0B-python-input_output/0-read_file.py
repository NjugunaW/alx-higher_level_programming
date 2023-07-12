#!/usr/bin/python3

"""
This module has a function that reads a text in UTF8 and
prints it to stdout
"""


def read_file(filename=""):
    """
    This function reads a file and prints it
    to stdout
    :filename:
    :return:
    """
    with open(filename, encoding="utf-8") as f_ile:
        print(f_ile.read(), end="")
