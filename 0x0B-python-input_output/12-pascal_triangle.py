#!/usr/bin/python3
"""module Pascals triangle"""


def pascal_triangle(n):
    """Function returns pascals tringle

    Args:
        n(int): the size of tringle beginining from 1

    Returns:
        Pascal's triangle.

    """
    p_row = [1]
    p_add = [0]
    p_Triangle = []
    if n <= 0:
        return p_Triangle
    for i in range(n):
        p_Triangle.append(p_row)
        p_row = [sum(i) for i in zip(p_row + p_add, p_add + p_row)]
    return p_Triangle
