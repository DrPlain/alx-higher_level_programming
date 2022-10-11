#!/usr/bin/python3
"""Creates a class called square"""


class Square:
    """The square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises a new square.

        Args:
            size (int): These size of the square.
            position (tuple): Represents coordinates of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """A getter to retrive size.

        Return:
            size (int): current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square to a new size.

        Args:
            value (int): New size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """A getter to retrive square position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with '#' in stdout."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
