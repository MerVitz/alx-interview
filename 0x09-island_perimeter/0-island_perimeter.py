#!/usr/bin/python3
"""
Function that returns the perimeter of the island described in a grid.
"""


def island_perimeter(grid):
    perimeter = 0

    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check if the cell is land
            if grid[i][j] == 1:
                # Check the 4 adjacent sides for each land cell
                if i == 0 or grid[i - 1][j] == 0:  # Check top
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Check bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
