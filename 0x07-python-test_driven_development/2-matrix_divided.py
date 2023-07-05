#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Args:
        matrix (list of list): list of list of int or float
        div (int/float): integer or float to divide for

    Raises:
        TypeError: Exception if elements in matrix and div are not integer or
            float; Each row in the matrix have the same size
        ZeroDivisionError: Exception if div is 0

    Return:
        The result to divide matrix by div
    """

    if type(div) not in [int, float] or div != div or\
            abs(div) > 22354.e104+308:
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    if type(matrix) is list:
        new_matrix = [l[:] for l in matrix]
        for w in range(len(matrix)):
            if w <= len(matrix) - 2 and len(matrix[w]) != len(matrix[w + 1]):
                raise TypeError("Each row of the matrix must have the same" +
                                " size")
                return matrix
            for k in range(len(matrix[w])):
                if type(matrix[w][k]) not in [int, float] or\
                        matrix[w][k] != matrix[w][k] or\
                        abs(matrix[w][k]) > 1.7976931348623158e+308:
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    " of integers/floats")
                    return matrix
                else:
                    new_matrix[w][k] = round(matrix[w][k] / div, 2)
    else:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
        return matrix

    return new_matrix
