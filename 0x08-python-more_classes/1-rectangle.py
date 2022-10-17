#!/usr/bin/python3
"""Creates a rectangle class"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Creates a Rectangle

        Args:
            width: optional argument with default 0
            height: optional argument with default 0

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less < 0
        """

        self.height = height
        self.width = width

    @property
    def height(self):
        """Gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height to the value passed"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width to the value passed"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
