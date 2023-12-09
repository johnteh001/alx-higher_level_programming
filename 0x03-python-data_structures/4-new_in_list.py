#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element.
        element: The new element to be placed at the specified index.

    Returns:
        list: A new list with the replacement (or a copy of the original list if index is out of range).
    """
    new_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element
    return new_list
