#!/usr/bin/python3
"""This Is Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This Is Square Class"""

    def __init__(self, size):
        """This Is Square Constructor"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
