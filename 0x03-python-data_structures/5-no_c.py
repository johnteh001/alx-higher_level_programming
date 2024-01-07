#!/usr/bin/python3
def no_c(my_string):
    """Function removes all characters c and c from a string."""
    new_string = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_string = new_string + i
    return new_string
