#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints an integer and returns True if successful.
    Otherwise, returns False and prints the error in stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
