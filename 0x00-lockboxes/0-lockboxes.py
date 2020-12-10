#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Method to check if all boxes can be opened 
    """
    if len(boxes) == 0:
        return False

    keys = [0]
    seen = 1
    for key in keys:
        for i in boxes[key]:
            if i not in keys:
                if i != key and i < len(boxes):
                    keys.append(i)
                    seen += 1
    if seen != len(boxes):
        return False
    return True
