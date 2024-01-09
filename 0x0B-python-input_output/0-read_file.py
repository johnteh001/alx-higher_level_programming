#!/usr/bin/python3
"""module reads text file"""


def read_file(filename=""):
    """Function reads text file and prints in stdout.

    Args:
        filename(obj)

    """
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end='')
