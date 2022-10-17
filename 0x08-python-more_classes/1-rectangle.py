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

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width attribute"""
        return self.__width

    @width_setter
    def width(self):
        """Sets width to the value passed"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height attribute"""
        return self.__height

    @height_setter
    def width(self):
        """Sets height to the value passed"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

