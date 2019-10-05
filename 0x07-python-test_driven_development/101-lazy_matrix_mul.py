#!/usr/bin/python3
"""
This module multiplies 2 matrices (numpy):
See:
    ./101-main.py test file
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Method to multyply two matrices (numpy)
    """
    import numpy as np
    return np.matmul(m_a, m_b)
