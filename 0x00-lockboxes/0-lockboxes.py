#!/usr/bin/python3
"""
Check if all boxes can opened
"""


def canUnlockAll(boxes):
    """
    RULES:
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    key_list = boxes[0].copy()
    true_keys = [0]
    len_box = len(boxes) - 1

    for id, key in enumerate(key_list):
        if key > len_box:
            continue
        else:
            for x in boxes[key]:
                if x not in key_list:
                    if x <= len_box:
                        key_list.append(x)
            if key not in true_keys:
                true_keys.append(key)

    return len(true_keys) == len(boxes)
