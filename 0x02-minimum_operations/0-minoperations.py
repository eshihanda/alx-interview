#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result
in exactly n H characters in the file.

"""


def minOperations(n):
    op_count = 0
    number = 2
    if type(n) is not int or n <= 1:
        return op_count
    while n > 1:
        if n % number == 0:
            op_count += number
            n /= number
        else:
            number += 1
    return(op_count)
