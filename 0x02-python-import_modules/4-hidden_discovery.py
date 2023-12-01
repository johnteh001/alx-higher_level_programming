#!/usr/bin/python3
"""
This script prints all the names defined by the compiled module hidden_4.pyc.
"""

import dis
import sys

if __name__ == "__main__":
    module = __import__('hidden_4')
    names = dir(module)

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)

