#!/usr/bin/python3
"""Creates a class called square"""


class Square:
    """The square class."""

    def __init__(self, size=0):
        """Initialises a new square.

        Args:
            size (int): These size of the square.
        """
        self.size = size

    @property
    def size(self):
        """A getter to retrive size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area."""
        return self.__size * self.__size
