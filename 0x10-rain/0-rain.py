#!/usr/bin/python3
"""
0-rain , calculate how much water will be retained after it rains.
"""


def rain(walls):
    """
    Args:
        walls :  is a list of non-negative integers.
    Returns:
        Integer indicating total amount of rainwater retained.
    """
    l_walls = len(walls)
    retained_water = 0

    for i in range(1, l_walls - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]

        for j in range(i + 1, l_walls):
            right = max(right, walls[j])

        retained_water = retained_water + (min(left, right) - walls[i])
    return retained_water