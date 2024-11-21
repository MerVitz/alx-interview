#!/usr/bin/python3
"""
Module to rotate a 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given nxn 2d matrix by 90 degrees clockwise in-place
    Args:
        matrix(list of list): The 2d matrix to rotate.
    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # swap elements at possitions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
