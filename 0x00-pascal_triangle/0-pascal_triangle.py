#!/usr/bin/python3
"""
0-pascal_triangle.py
Defines a function that generates Pascal's Triangle.
"""

def pascal_triangle(n):
    """Generate Pascal's Triangle with n rows."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)

        # Fill in values, skipping the first and last element
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the row to the triangle

    return triangle
