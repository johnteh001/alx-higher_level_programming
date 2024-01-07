#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Function deletes the item at a given position within a my_list."""
    size = len(my_list)
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(size):
        if i == idx:
            del my_list[i]
    return my_list
