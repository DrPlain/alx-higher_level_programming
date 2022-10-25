#!/usr/bin/python3
"""BaseGeometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry"""

    def __init__(self, width, height):
        """object constructor

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
