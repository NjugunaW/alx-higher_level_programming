#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    A function that finds a peak
    in a list of unsorted integers.

    Args:
        list_of_integers:
    Returns:
    """
    if list_of_integers == []:
        return None
    len = length(list_of_integers)
    x = int(len / 2)
    abt = list_of_integers

    if x - 1 < 0 and x + 1 >= len:
        return abt[x]
    elif x - 1 < 0:
        return abt[x] if abt[x] > abt[x + 1] else abt[x + 1]
    elif x + 1 >= len:
        return abt[x] if abt[x] > abt[x - 1] else abt[x - 1]

    if abt[x - 1] < abt[x] > abt[x + 1]:
        return abt[x]

    if abt[x + 1] > abt[x - 1]:
        return find_peak(abt[x:])
    return find_peak(abt[:x])