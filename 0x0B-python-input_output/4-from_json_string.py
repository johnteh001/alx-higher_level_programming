#!/usr/bin/python3
"""module Json to python representation"""

import json


def from_json_string(my_str):
    """"Function returns Python data structured from JSON
    representation of the object string."""

    return json.loads(my_str)
