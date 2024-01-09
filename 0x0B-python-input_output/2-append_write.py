#!/usr/bin/python3
"""module appends a string to text file"""


def append_write(filename="", text=""):
    """Function appends a string to a text file

    Args:
        filename(obj): the text file
        text(str): the string text

    Returns:
        number of characters written.

    """
    with open(filename, 'a') as f:
        x = f.write(text)
        return x
