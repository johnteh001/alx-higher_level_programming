#!/usr/bin/python3
"""module creates object from json file"""

import json


def load_from_json_file(filename):
    """convert json text to python object.

    Args:
        filename(obj): file name

    """
    with open(filename, 'r') as f:
        text = f.read()
        return json.loads(text)
