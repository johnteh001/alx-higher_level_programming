#!/usr/bin/python3
"""Square module - defines square area and checks for errors."""


class Square:
    """Square defines the object square using private attribute __size.


    Attributes:
        __size: Instance variable of class square.


        """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area - finds the area of the square.


        Return:
            area of the square.


        """
        return (self.__size * self.__size)
