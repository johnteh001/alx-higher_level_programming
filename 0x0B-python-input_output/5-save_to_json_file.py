#!/usr/bin/python3
"""module sabe object to file"""

import json


def save_to_json_file(my_obj, filename):
    """saves object to text file.

    Args:
        my_obj(obj): object to be converted to JSON
        filename(obj): file name

    """
    with open(filename, 'w') as f:
        text = json.dumps(my_obj)
        f.write(text)
