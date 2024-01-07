#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """Function divides a list matrix using div.

    Args:
        matrix(int,float): integers or floats to be divided
        div(int, flaot): divider value

    Return:
        new_matrix(int,float): result of the division

    Raises:
        TypeError: if the matrix is not list of list, integer, or float
        ZeroDivisionError: if div is zero

    """

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    rows = []
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) of' +
                        ' integers/floats')
    c = len(matrix[0])
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists)' +
                                ' of integers/floats')
            if len(i) != c:
                raise TypeError('Each row of the matrix must have the' +
                                ' same size')
            rows.append(round((j / div), 2))
        new_matrix.append(rows)
        rows = []
    return (new_matrix)
