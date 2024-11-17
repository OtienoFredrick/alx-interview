#!/usr/bin/python3
"""
Solution to lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines whether all boxes can be unlocked.
    """
    if not isinstance(boxes, list) or not boxes:
        return False

    unlocked = [0]  # Start with the first box unlocked
    keys = set(boxes[0])  # Collect keys from the first box

    while keys:
        key = keys.pop()
        if key not in unlocked and 0 <= key < len(boxes):
            unlocked.append(key)
            keys.update(boxes[key])  # Add keys from the newly unlocked box

    return len(unlocked) == len(boxes)
