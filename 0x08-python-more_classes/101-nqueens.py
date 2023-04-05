#!/usr/bin/python3
"""This module contains functions to solve the N-Queens problem
"""


def backtrack(n):
    # create a board
    board = [[False for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    n = sys.argv.pop()
    try:
        n = int(n)
    except:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        backtrack(n)
