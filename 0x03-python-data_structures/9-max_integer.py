#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list."""
    if len(my_list) == 0:
        return None
    ln = my_list[0]
    for i in my_list:
        if i > ln:
            ln = i
    return ln
