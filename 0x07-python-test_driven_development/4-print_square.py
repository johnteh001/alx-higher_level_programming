#!/usr/bin/python3
"""Print square module of size"""


def print_square(size):
    """print_square uses '#' to print square.

    Args:
        size(int): size of the square

    Raises:
        TypeError: if the size is not an integer
        ValueError: if the size is less than 0

    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            if j != size - 1:
                print('#', end='')
                continue
            print('#')
