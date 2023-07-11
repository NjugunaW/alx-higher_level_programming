#!/usr/bin/python3
"""
This module returns a list of lists 
of integers representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    This module returns a list of lists 
    of integers representing the Pascal’s triangle of n.

    Args:
        int (n): Integer     

    Returns:
           a list of lists of integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        xyz = triangle[-1]
        arbtry = [1]
        for i in range(len(xyz) - 1):
            arbtry.append(xyz[i] + xyz[i + 1])
        arbtry.append(1)
        triangle.append(arbtry)
    return triangle
