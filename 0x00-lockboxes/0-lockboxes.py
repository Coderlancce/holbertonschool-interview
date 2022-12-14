#!/usr/bin/python3
"""
"""


def canUnlockAll(boxes):
    """
    """
    keys = boxes[0]
    size = len(boxes)
    aux = 1
    while size > aux:
        print("im here")
        for key in keys:
            print("key: {}".format(key))
            if aux == key:
                keys.extend(boxes[aux])
                break
        aux+=1
    return True
