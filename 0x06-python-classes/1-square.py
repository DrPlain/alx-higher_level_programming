#!/usr/bin/python3
"""Creates a class called square"""

class Square:
    """The square class.
        
    Args:
        size (int): Size of the square

    Attribute:
        size(int): Size of the square

    """
    def __init__(self, size):
        """Initialises instances of the class"""

        self._size = size
