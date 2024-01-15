#!/usr/bin/python3
"""Module base"""
import json
import csv
from collections import OrderedDict
import turtle


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that initializes the public instance attribute id
        Args:
            id(int): integer value to manage the id
        Rreturn:
            Always nothing.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_object
