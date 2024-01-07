def add_integer(a, b=98):
    """Adds two integers together.

    Args:
        a: The first integer to add.
        b: The second integer to add. Defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
