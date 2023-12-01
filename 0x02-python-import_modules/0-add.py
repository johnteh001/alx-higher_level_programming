#!/usr/bin/python3
"""
This module imports the add function and prints the result of the addition.
"""

a = 1
b = 2
add_0 = __import__('add_0')
print("{} + {} = {}".format(a, b, add_0.add(a, b)))
