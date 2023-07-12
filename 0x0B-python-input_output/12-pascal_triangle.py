#!/usr/bin/python3
"""
This module has a function that returns a list of lists of
integers representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of 
    integers representing the Pascal’s triangle of n
    :n:
    :return:
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        bse = triangle[-1]
        temp = [1]
        for x in range(len(bse) - 1):
            temp.append(bse[x] + bse[x + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
