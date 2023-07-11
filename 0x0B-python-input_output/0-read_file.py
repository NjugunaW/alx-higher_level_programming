#!/usr/bin/python3

def read_file(filename=""):

    """
    This module reads a text file and prints it to stdout

    Args:
        filename (filedes): The file to be opened
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")


