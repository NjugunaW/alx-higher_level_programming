#!/usr/bin/python3
"""
This module appends a string 
at the end of a text file
"""

def append_write(filename="", text=""):
    """
    This module appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    :filename:
    :text:
    :return: Number of characters added
    """
    with open(filename, 'a', encoding='utf') as f_ile:
        return f_ile.write(text)
