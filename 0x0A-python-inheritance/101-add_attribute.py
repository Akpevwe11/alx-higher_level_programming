#!/usr/bin/python3
"""Defines a function that adds attribuutes to objects"""


def add_atttribute(obj, att, value):
    """Add a new attribute to an object."""

    if not hasattr(obj, "__dict_"):
        raise TypeError("can't add new atttribute")
    setattr(obj, att, value)
