#!/usr/bin/python3
"""A module that adds two numbers

The numbers can either be integers or floats.

It adds both positive and negative elements

"""


def add_integer(a, b=98):
    """Adds two numbers

    Performs the addition between two numbers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int: The result of the addition.

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    """
    Converts a float num to an int num

    Args:
        num (int, float): The number to cast.

    Returns:
        int: The number converted to  an integer.

    """
    if type(num) is float:
        num = int(num)
        return num

    return num
