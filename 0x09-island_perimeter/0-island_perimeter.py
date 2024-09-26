#!/usr/bin/python3
'''
Island Perimeter
'''


def island_perimeter(grid) -> int:
    '''
        returns the perimeter of the island described in grid
        grid is a list of list of integers
        0 represents water
        1 represents land

    '''
    row, col = len(grid), len(grid[0])
    land, perimeter = 0, 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                land += 1
                if i < row-1 and grid[i+1][j] == 1:
                    perimeter += 1
                if j < col-1 and grid[i][j+1] == 1:
                    perimeter += 1
    return land*4-2*perimeter
