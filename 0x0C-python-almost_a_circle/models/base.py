#!/usr/bin/python3
"""Module containing Base class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of Base

        Args:
            id(int): Object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
