#!/usr/bin/python3
"""this module print square"""


def print_square(size):
    """
    This Function Draw a Rectangular
    Args:
        size (int): must be an int to draw the square
    Returns:
        a square printed to stdout
    """
    if not isinstance(size, int):
        raise TypeError("size must be integer")
    if size <= 0:
        raise ValueError("size must be greather than 0")
    txt = "#" * size
    for i in range(size):
        print(txt)
