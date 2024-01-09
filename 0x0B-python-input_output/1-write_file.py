#!/usr/bin/python3
"""module writes a string to text file"""


def write_file(filename="", text=""):
    """Function writes a string to a text file

    Args:
        filename(obj): the text file
        text(str): the string text

    Returns:
        number of characters written.

    """
    with open(filename, 'w') as f:
        x = f.write(text)
        return x
