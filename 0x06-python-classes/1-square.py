#!/usr/bin/python3
"""Creates a class called square"""


class Square:
    """The square class."""

    def __init__(self, size=0):
        """Initialises a new square.

        Args:
            size (int): These size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must not be less than 0")
        self.__size = size
