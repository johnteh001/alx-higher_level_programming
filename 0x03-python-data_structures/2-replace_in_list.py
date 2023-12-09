#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position.

    Args:
        my_list (list): The input list.
        idx (int): The index where the element should be replaced.
        element: The new element to replace at the specified index.

    Returns:
        list: The modified list or the original list if index is out of range.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
