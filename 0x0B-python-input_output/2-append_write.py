#!/usr/bin/python3
"""
This module appends a string at the end of a text file
"""

def append_write(filename="", text=""):
    """
    This module appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (flds): Name of the file
        text (string): String to append

    Returns: 
        returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
