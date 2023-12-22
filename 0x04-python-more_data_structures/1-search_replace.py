#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element in a list."""
    return [replace if item == search else item for item in my_list]
