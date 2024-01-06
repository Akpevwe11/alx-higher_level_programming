#!/usr/bin/python3
"""add two integer module"""


def add_integer(a, b=98):
    """
    Add two Numbers and return The Result as (int)
    Args:
        a (int): the first number
        b (int): the second number
    Returns:
        int: the sum of two numbers
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    if a in [float('inf'), float('-inf')]:
        raise TypeError("a must be an integer not float infinity")
    if b in [float('inf'), float('-inf')]:
        raise TypeError("b must be an integer not float infinity")
    return int(a) + int(b)
