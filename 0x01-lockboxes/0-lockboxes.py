#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list where each sublist represents a box and contains keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = {0}  # Set of opened boxes, starting with box 0
    keys = set(boxes[0])  # Keys obtained from the first box

    while keys:
        new_keys = set()
        for key in keys:
            if key < n and key not in opened:
                opened.add(key)
                new_keys.update(boxes[key])

        # Break if no new boxes can be opened
        if not new_keys.difference(opened):
            break

        # Update keys to only those that open unopened boxes
        keys = new_keys.difference(opened)

    return len(opened) == n

