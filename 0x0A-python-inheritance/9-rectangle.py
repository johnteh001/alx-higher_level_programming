#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Class

    Atributes:
            area: raises exception

    Raises:
        Exception with error message.

    """

    def area(self):
        return Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value.

        Args:
            name(str)
            value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero

        """
        if type(value) is not int:
            raise TypeError(str(name) + ' must be an integer')
        if value <= 0:
            raise ValueError(str(name) + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """Rectangle is a subclass of BaseGeometry."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Obtains the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Obtains the string representation"""

        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
