#!/usr/bin/python3
"""
0. Island Perimeter
"""

def island_perimeter(grid):
    """
    Args:
        grid ([list]): [list of list of integers]
    Returns:
        [int]: [perimeter of the island described in grid]
    """
    perimeter = 0
    l_grid = len(grid)
    if l_grid == 0:
        return 0
    n = len(grid[0])
    for i in range(l_grid):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += 4
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter