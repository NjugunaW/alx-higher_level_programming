#!/usr/bin/python3

"""
This module reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    This module reads a text file and prints it to stdout
    
    Args:
        filename (flds): Name of file to be opened

    :return:
    """
    with open(filename, encoding="utf-8") as f_ile:
        print(f_ile.read(), end="")
