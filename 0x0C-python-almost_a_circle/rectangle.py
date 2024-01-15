#!/usr/bin/python3
"""Defines a rectangle module (modules.rectangle)"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that init values for a rectangle object
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: Variable x
            y: Variable y
        Return: 
            Nothing
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Getter for the triangle width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """Setter for the width
            Args:
                value: value to assign for the width size
            Return:
                Nothing
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

            # Getter and setter for the height of the reactangle
            @property
            def height(self):
                """Getter for the height value
                """
                return self.__height

            @height.setter
            def height(self, value):
                """setter for the height
                Args:
                    value: size to assign to the height
                Return:
                    Always returns Nothing
                """
                if type(value) is not int:
                    raise TypeError("height must be an integer")
                elif value <= 0:
                    raise ValueError("height must be > 0")
                else:
                    self.__height = value

            # Getter and setter for y variable
            @property
            def y(self):
                """Getter of y variable
                """
                return self.__y

            @y.setter
            def y(self, value):
                """Setter of y variable
                Args:
                    value: value to assign to y variable
                Return:
                    Returns nothing
                """
                if type(value) is not int:
                    raise TypeError("y must be an integer")
                elif value < 0:
                    raise ValueError("y must be >=0")
                else:
                    self.__y = value

            def area(self):
                """Method that returns the area of the rectangel object
                Args:
                    Not arguments
                Return:
                    Area of the rectangle objec
                """
                return self.width * self.height


