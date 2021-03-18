#!/usr/bin/python3
"""
0. N queens
"""
import sys
BOARD_SIZE = sys.argv[1]


def under_attack(col, queens):
    """
    [check if a queen is under attack]
    """
    return col in queens or any(abs(col - x) == len(queens) - i
                                for i, x in enumerate(queens))


def solve(BOARD_SIZE):
    """
    [FIND SOLUTION]
    """
    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        exit(1)
    if not (sys.argv[1]).isdigit():
        print("N must be a number")
        exit(1)
    BOARD_SIZE = int(sys.argv[1])
    if BOARD_SIZE < 4:
        print("N must be at least 4")
        exit(1)
    solutions = [[]]
    for row in range(BOARD_SIZE):
        solutions = [solution+[i]
                     for solution in solutions
                     for i in range(BOARD_SIZE)
                     if not under_attack(i, solution)]
    return solutions


for answer in solve(BOARD_SIZE):
    print(list(enumerate(answer)))
