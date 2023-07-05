#!/usr/bin/python3
"""

This module prints a text with a 2 new lines after each of
these characters: `.`, `?`, `:`

Example:

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
    $
    Quonam modo?$
    $
    
    * text must be a string

    * There should be no space at the beginning or
    at the end of each printed line

"""


def text_indentation(text):
    """

    Prints a text with indentation

    Args:
        text (str): The text to prints.

    Raises:
        TypeError: If `text` isn't string.

    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    txt_size = len(text)
    obj = 0
    frsh_str = ''
    commence = True

    while obj < txt_size:
        if text[obj] == ' ' and commence is True:
            obj += 1
            continue

        commence = False

        if text[obj] in '.?:':
            frsh_str += text[obj]
            frsh_str += '\n'
            frsh_str += '\n'
            obj += 1

            while obj < txt_size and text[obj] == ' ':
                obj += 1

            continue

        if obj < txt_size:
            frsh_str += text[obj]
            obj += 1

    print(frsh_str, end='')
