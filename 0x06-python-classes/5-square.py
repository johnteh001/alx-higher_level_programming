#!/usr/bin/python3
"""Square module - provides setter and getter properties."""


class Square:
    """Square defines the object square using private attribute __size.


    Attributes:
        __size: Instance variable of class square.


        """

    def __init__(self, size=0):
        """__init__ - initializes the square."""

        self.size = size

    @property
    def size(self):
        """Obtains value of size.

        Raises:
            TypeError: Occurs when size is not integer.
            ValueError: Occurs when size is less than 0

        """

        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the size."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area - finds the area of the square.


        Return:
            area of the square.


        """
        return (self.__size * self.__size)

    def my_print(self):
        """my_print - prins in stdout the square with character #."""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end='')
            print()
