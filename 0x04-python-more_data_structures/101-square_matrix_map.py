#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return (list(map(lambda w: list(map(lambda a: a**2, w)), matrix)))
