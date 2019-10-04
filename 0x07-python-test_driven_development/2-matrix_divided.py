#!/usr/bin/python3
"""
This module divides all elements of a matrix.
See:
    ./2-main.py test file
"""


def matrix_divided(matrix, div):
    """
    Method that divides elements on matrix
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(message)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(message)
    new_matrix = []
    for row in matrix:
        div_matrix = []
        for i in row:
            elem = round(i / div, 2)
            div_matrix.append(elem)
        new_matrix.append(div_matrix)
    return new_matrix
