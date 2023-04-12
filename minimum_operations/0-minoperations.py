#!/usr/bin/python3
"""
Check the number of operations "copy, paste" for get the number n
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    operations = 0
    sum = 1
    carrier = 0

    while sum < n:
        if n % sum == 0: #calculate if n is multiple of them
            carrier = sum # save the last copy
            sum *= 2 # paste
            operations += 1 # sum the copy operation
        else: # if no are multiple i need a mulple
            sum += carrier # alone paste
        operations += 1 # sum the paste operation
    
    return operations