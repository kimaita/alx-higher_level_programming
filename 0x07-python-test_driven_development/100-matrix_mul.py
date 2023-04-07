#!/usr/bin/python3
"""This module contains a function for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices

    Args:
        m_a (_type_): _description_
        m_b (_type_): _description_
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if any(not isinstance(x, list) for x in m_a):
        raise TypeError('m_a must be a list of lists')
    if any(not isinstance(x, list) for x in m_b):
        raise TypeError('m_b must be a list of lists')
    if not any(m_a):
        raise ValueError("m_a can't be empty")
    if not any(m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError('m_a should contain only integers or floats')
    if any(not isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError('m_b should contain only integers or floats')
    len_row = len(m_a[0]), len(m_b[0])
    if any(len(row) != len_row[0] for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if any(len(row) != len_row[1] for row in m_b):
        raise TypeError('each row of m_b must be of the same size')
    if len_row[0] != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product = []
    for r in range(len(m_a)):
        row_mult = []
        for c in range(len_row[1]):
            rc_sum = 0
            for idx, elem in enumerate(m_a[r]):
                rc_sum += elem * m_b[idx][c]
            row_mult.append(rc_sum)
        product.append(row_mult)

    return product
