#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    function to rotate a 2D matrix 90 degrees clockwise
    """
    row = len(matrix)
    col = len(matrix[0])
    row_m = [[0 for i in range(row)] for j in range(col)]
    col_m = matrix[:]
    i = 0
    while i < row:
        j = 0
        while j < col:
            row_m[j][len(col_m) - 1 - i] = col_m[i][j]
            j += 1
        matrix.pop()
        i += 1

    i = 0
    while i < col:
        matrix.append(row_m[i])
        i += 1