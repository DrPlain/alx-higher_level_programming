#!/usr/bin/python3
"""Contains the function is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of specified class
    Args:
        obj: instance of class a_class
        a_class: class
    """

    if type(obj) == a_class:
        return True
    return False
