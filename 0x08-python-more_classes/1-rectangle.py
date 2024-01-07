#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class gives basic description of a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Obtains and sets the width of rectangle.

        Raises:
            TypeError: When the widht is not integer
            ValueError: When width < 0

        """

        return self.__width

    @width.setter
    def width(self, value):
        """sets width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Obtains the height of the rectangle.

        Raises:
            TypeError: when height is not integer.
            ValueError: When height < 0

        """

        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of rectangle height"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
