#!/usr/bin/python3
"""
Defines the class MyList
"""


class MyList(list):
    """A subclass that inherits from list as superclass"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
