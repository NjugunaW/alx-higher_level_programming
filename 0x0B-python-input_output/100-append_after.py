#!/usr/bin/python3
"""
A module that inserts a line of text to a file, 
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A module that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (flds): Name of file
        search_string (str): Old String
        new_string (str): Appended string   
    """
    with open(filename, 'r', encoding='utf-8') as f_ile:
        line_list = []
        while True:
            line = f_ile.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f_ile:
        f_ile.writelines(line_list)
