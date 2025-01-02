#!/usr/bin/python3
"""
Function that returns the perimeter of the island described in a grid.
The grid is a 2D list of integers where 1 represents
land and 0 represents water.
The perimeter is calculated by considering the edges of land
cells that are adjacent to water or the grid boundary.

Parameters:
    grid (list of list of integers): A 2D grid where 1
    represents land and 0 represents water.

Returns:
    int: The perimeter of the island.
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a 2D grid."""
    perimeter = 0

    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If we find land (cell with value 1)
            if grid[i][j] == 1:
                # Check if the top edge is exposed
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check if the bottom edge is exposed
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check if the left edge is exposed)
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check if the right edge is exposed)
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
