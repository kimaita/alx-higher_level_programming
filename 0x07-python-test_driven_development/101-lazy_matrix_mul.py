#!/usr/bin/python3
"""This modules contains a function for matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Uses the NumPy library for matrix multiplication

    Args:
        m_a (list): the first matrix
        m_b (list): the second matrix
    """
    return np.matmul(m_a, m_b)
