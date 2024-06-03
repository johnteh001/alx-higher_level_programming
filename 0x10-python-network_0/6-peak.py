#!/usr/bin/python3
"""Find peak"""


def find_peak(list_of_integers):
    """finding peak of list of integers

    Arguments:
        list_of_integers (list): list of integers

    Returns:
        peak(int): the peak of the list
    """
    arr = list_of_integers
    length = len(arr)
    if length is None:
        return None
    if length == 1:
        return arr[0]
    if (length == 2 and arr[0] >= arr[1]):
        return arr[0]
    if length > 2:
        if (arr[length - 1] >= arr[length - 2]):
            return arr[length - 1]
        for i in range(1, length):
            if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
                return arr[i]
        return arr[0]
