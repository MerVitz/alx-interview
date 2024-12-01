#!/usr/bin/python3
"""
Module for calculating the minimum operations to achieve `n` characters
using only Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.

    Parameters:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations needed, or 0 if impossible.
    """
    if n < 2:
        return 0  # Impossible to create less than 2 characters

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

