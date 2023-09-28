#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    A function that finds a peak in a list of unsorted integers.
    """
    if list_of_integers == []:
        return None

    _length_ = len(list_of_integers)
    avrg = int(_length_ / 2)
    frsh_lst = list_of_integers

    if avrg - 1 < 0 and avrg + 1 >= _length_:
        return frsh_lst[avrg]
    elif avrg - 1 < 0:
        return frsh_lst[avrg] if frsh_lst[avrg] > frsh_lst[avrg + 1] \
            else frsh_lst[avrg + 1]
    elif avrg + 1 >= _length_:
        return frsh_lst[avrg] if frsh_lst[avrg] > frsh_lst[avrg - 1] \
            else frsh_lst[avrg - 1]

    if frsh_lst[avrg - 1] < frsh_lst[avrg] > frsh_lst[avrg + 1]:
        return frsh_lst[avrg]

    if frsh_lst[avrg + 1] > frsh_lst[avrg - 1]:
        return find_peak(frsh_lst[avrg:])
    return find_peak(frsh_lst[:avrg])
