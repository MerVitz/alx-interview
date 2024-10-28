#!/usr/bin/python3
"""
0-pascal_triangle.py
Return a empty list if n <=0
Initialize the triangle as an empty list
"""
def pascal_triangle(n):
    """Generate Pascal's Triangle with n rows."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)

        # Fill in the values (skip the first and last element since they're always 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the row to the triangle

    return triangle

