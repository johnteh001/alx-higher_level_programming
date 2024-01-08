#!/usr/bin/python3
"""Module determines if object is instance of specified class."""


def inherits_from(obj, a_class):
    """Function determines if object is an instance of a class.

    Args:
        obj(obj): object to be determined
        a_class: class to be checked

    Returns:
        True(bool): if object is an instance of class it direclty
            inherited from
        False(bool): Otherwise.

    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
