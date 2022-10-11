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
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current square area.

        Return:
            area (int): The current area of the square.
        """
        return self.__size * self.__size
