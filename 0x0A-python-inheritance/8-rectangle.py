#!/usr/bin/python3
"""this is rectangle class definition"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """this is rectangle class definition"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_valiidator("height", height)
        self.__width = width
        self.__height = height
