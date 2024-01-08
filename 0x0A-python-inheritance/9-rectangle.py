#!/usr/bin/python3
"""this is rectangle class definition"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """this is rectangle class definition"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """this calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """this returns a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
