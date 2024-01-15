#!/usr/bin/python3
"""this is Rectangle Classes"""
from .base import Base


class Rectangle(Base):
    """this is Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def check_for_type(self, value, attr):
        """this checks for value is int"""
        if type(value) != int:
            raise TypeError(f"{attr} must be an integer")

    def check_for_dimensions(self, value, attr):
        """this checks dimensions"""
        self.check_for_type(value, attr)
        if value <= 0:
            raise ValueError(f"{attr} must be > 0")

    def check_for_coordinates(self, value, attr):
        """this checks for coordinates values if int and >= 0"""
        self.check_for_type(value, attr)
        if value < 0:
            raise ValueError(f"{attr} must be >= 0")

    @property
    def width(self):
        """this is Rectangle Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this is Rectangle Width Setter"""
        self.check_for_dimensions(value, "width")
        self.__width = value

    @property
    def height(self):
        """this is Rectangle Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this is Rectangle Height Setter"""
        self.check_for_dimensions(value, "height")
        self.__height = value

    @property
    def x(self):
        """this is Rectangle X"""
        return self.__x

    @x.setter
    def x(self, value):
        """this is Rectangle X Setter"""
        self.check_for_coordinates(value, "x")
        self.__x = value

    @property
    def y(self):
        """this is Rectangle Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """this is Rectangle Y Setter"""
        self.check_for_coordinates(value, "y")
        self.__y = value

    def area(self):
        """this is Rectangle Area"""
        return self.width * self.height

    def display(self):
        """this is Rectangle Display"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(f"{' ' * self.x}{'#'*self.width}")

    def __str__(self):
        """this is Rectangle String Representation"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """this is updating using args"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            for index, value in enumerate(args):
                setattr(self, attr[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
