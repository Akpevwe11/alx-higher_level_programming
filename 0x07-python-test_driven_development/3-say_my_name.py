#!/usr/bin/python3
"""the moudle responsable to print firstname, lastname"""


def say_my_name(firstname, lastname=""):
    """
    this function takes firstname, lastname and
    print it in format My name is <firstname> <lastname>
    Args:
        firstname (str): the user firstname
        lastname (str): the user firstname
    Returns:
        My name is <firstname> <lastname>
    """
    if firstname is None:
        raise TypeError("firstname must be a not null")
    if not isinstance(firstname, str):
        raise TypeError("firstname must be a string")
    if not isinstance(lastname, str):
        raise TypeError("lastname must be a string")
    if len(firstname) == 0:
        raise ValueError("firstname must vaild name")
    return f"My name is {firstname}{lastname}"
