#!/usr/bin/python3
"""Module determines if object is instance of specified class."""


def is_same_class(obj, a_class):
    """Function determines if object is an instance of a class.

    Args:
        obj(obj): object to be determined
        a_class: class to be checked

    Returns:
        True(bool): if object is an instance of class
        False(bool): Otherwise.

    """

    if type(obj) is (a_class):
        return True
    else:
        return False
