#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list.

    Args:
        my_list (list): List of integers.

    Format:
        One integer per line.

    Returns:
        None
    """
    for number in my_list:
        print("{:d}".format(number))
