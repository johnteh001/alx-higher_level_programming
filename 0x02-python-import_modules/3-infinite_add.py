#!/usr/bin/python3
"""
This program prints the result of the addition of all arguments.
"""

if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    result = 0

    for arg in args:
        result += int(arg)

    print(result)
