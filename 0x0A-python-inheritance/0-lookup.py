 #!/usr/bin/python3
""" lookup module determines the attributes and methods of an object."""


def lookup(obj):
    """Lookup function finds the list of attributes of an object.

    Returns:
        The list of available attributes and objects.

    """
    return(dir(obj))
