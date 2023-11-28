#!/usr/bin/python3

def islower(c):
    """
    Checks if the given character is lowercase.

    Args:
    - c: a character

    Returns:
    - True if c is lowercase, False otherwise
    """
    return ord('a') <= ord(c) <= ord('z')
