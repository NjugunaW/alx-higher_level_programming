#!/usr/bin/python3
"""
This module has a function that returns a list of
integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal’s triangle of n
    :n:
    :return:
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        ang = triangles[-1]
        temp = [1]
        for i in range(len(ang) - 1):
            temp.append(ang[i] + ang[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles

