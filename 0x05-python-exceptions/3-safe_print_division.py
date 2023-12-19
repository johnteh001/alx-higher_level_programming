#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Safely divides two integers and prints the result.

    Args:
        a: Integer dividend.
        b: Integer divisor.

    Returns:
        The result of the division, or None if an error occurs.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
