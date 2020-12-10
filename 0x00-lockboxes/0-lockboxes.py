#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Method to check if all boxes can be opened 
    """
    if not boxes or len(boxes) ==0:
        return False

    keys = [0]
    seen = 1
    for key in keys:
        for i in boxes[key]:
            if i not in keys:
                if i != key & i <len(boxes):
                    keys.append(i)
                    seen += 1
    return True