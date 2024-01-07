#!/usr/bin/python3
"""say_my_name module prints the name."""


def say_my_name(first_name, last_name=""):
    """say_my_name prints name.

    Args:
        first_name(str): first name
        last_name(str): last name

    Raises:
        TypeError: when the name is not string type

    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
