#!/usr/bin/python3
"""[pascal triangle]
"""


def pascal_triangle(n):
    """[def pascals_triangle]

    Returns : returns a list of lists of integers representing the Pascal’s triangle of n
    """
    res = []
    for i in range(n):
        element = [None for _ in range(i + 1)]
        element[0], element[-1] = 1, 1
        for j in range(1, len(element) - 1):
            element[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(element)
    return res