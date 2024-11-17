#!/usr/bin/python3
"""
You have n number of locked boxes
in front of you. Each box is numbered
sequentially from 0 to -1. Each box may
contain keys to the other lock boxes. This method
determines if all other boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all other boxes can be opened
    """
    # Check if the boxes is not a List or its len == 0
    if not isinstance(boxes, list):
        return False
    elif len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked_b = set()
    unlocked_b.add(0)
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key > n or key in unlocked_b:
            continue
        unlocked_b.add(key)
        keys.update(boxes[key])
    return len(unlocked_b) == n
