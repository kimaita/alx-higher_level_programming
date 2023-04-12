#!/usr/bin/python3
"""This module contains function to create a Pascal's triangle"""


def pascal_triangle(n):
    """Generates a Pascal's triangle for n

    Args:
        n (int): number to generate traingle of
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            n = triangle[i-1][j]+triangle[i-1][j-1]
            row.append(n)
        row.append(1)
        triangle.append(row)
    return triangle
