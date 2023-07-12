#!/usr/bin/python3
"""
A module that writes a string to a text file (UTF8) and 
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    This module writes a string to a text file (UTF8) and 
    returns the number of characters written

    Args:
        filename (flds): Name of file
        text (flds): Text to write

    Returns:
        number of chararacters written 
    """

    with open(filename, mode='w', encoding='utf') as f_ile:
        return f_ile.write(text)
