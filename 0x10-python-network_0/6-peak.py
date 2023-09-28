#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    A function that finds a peak
    in a list of unsorted integers.
    """
    if list_of_integers == []:
        return None
    _len_ = len(list_of_integers)
    x = int(_len_ / 2)
    abt = list_of_integers

    if x - 1 < 0 and x + 1 >= _len_:
        return abt[x]
    elif x - 1 < 0:
        return abt[x] if abt[x] > abt[x + 1] else abt[x + 1] \
            else abt[x + 1]
    elif x + 1 >= _len_:
        return abt[x] if abt[x] > abt[x - 1] \
            else abt[x - 1]

    if abt[x - 1] < abt[x] > abt[x + 1]:
        return abt[x]

    if abt[x + 1] > abt[x - 1]:
        return find_peak(abt[x:])
    return find_peak(abt[:x])