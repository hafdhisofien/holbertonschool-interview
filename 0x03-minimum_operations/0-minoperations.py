#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """

    if n <= 1:
        return 0
    input = n
    div = 2
    i = 0

    while input > 1:
        if input % div == 0:
            input = input / div
            i = i + div
        else:
            div += 1
    return i
