#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order.

    Args:
        my_list (list): List of integers.

    Format:
        One integer per line, in reverse order.

    Returns:
        None
    """
    reversed_list = my_list[::-1]
    for number in reversed_list:
        print("{:d}".format(number))
