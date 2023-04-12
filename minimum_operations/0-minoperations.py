#!/usr/bin/python3
"""
Check the number of operations "copy, paste" for get the number n
"""

def minOperations(n):
    """
    call getPrimo function and sum the answer for get the minOperations
    """
    accum = 0
    while n > 1:
        primo = getPrimo(n)
        n /= primo
        accum += primo
    
    return accum

def getPrimo(n):
    """
    check what primo number can use for get the result
    """
    primos = [2, 3, 5, 7, 11]
    for i in primos:
        if n % i == 0:
            return i