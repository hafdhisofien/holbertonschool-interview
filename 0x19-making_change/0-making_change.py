#!/usr/bin/python3
"""
0. Change comes from within
"""

import sys


def makeChange(coins, total):
    """[summary]
    determine the fewest number of [coins] needed
    to meet a given amount [total]
    Args:
        coins : number of coins
        total : Total number of coins
    Returns:
        fewest number of coins needed
    """
    if (total <= 0):
        return 0
    max_n = len(coins)
    table = [0 for i in range(total + 1)]
    table[0] = 0
    for i in range(1, total + 1):
        table[i] = sys.maxsize
    for i in range(1, total + 1):
        for j in range(max_n):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    if table[total] == sys.maxsize:
        return -1
    return table[total]
