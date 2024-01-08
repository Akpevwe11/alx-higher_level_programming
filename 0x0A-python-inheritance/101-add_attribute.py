#!/usr/bin/python3
"""this add new attributes to the current object"""


def add_attribute(obj, name, value):
    """add a attribute to an object"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
