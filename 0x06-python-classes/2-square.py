#!/usr/bin/python3

class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialization method with optional size.

        Args:
            size (int): Size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size