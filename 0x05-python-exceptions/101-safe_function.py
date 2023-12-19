#!/usr/bin/python3
def safe_function(fct, *args):
    """
    Executes a function safely.

    :param fct: Pointer to a function
    :param args: Arguments to pass to the function
    :return: Result of the function, or None if an exception occurs
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
