#!/usr/bin/python3
""" This module prints the pascal triangle
See:
    ./14-main.py test file
"""


def pascal_triangle(n):
    """
    Pascal algor.
    """
    mtx = [[0 for j in range(i + 1)] for i in range(n)]
    for line in range(n):
        for i in range(line + 1):
            if i is 0 or i is line:
                mtx[line][i] = 1
            else:
                mtx[line][i] = mtx[line - 1][i - 1] + mtx[line - 1][i]
    return(mtx)
