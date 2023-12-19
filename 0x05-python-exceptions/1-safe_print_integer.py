#!/usr/bin/python3
def safe_print_integer(value):
    """
    Safely prints an integer.

    Args:
        value: Any type (integer, string, etc.)

    Returns:
        True if value has been correctly printed (integer), False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
