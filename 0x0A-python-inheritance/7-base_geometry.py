#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry():
    """class BaseGeometry"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating parameters.

        Args:
            name(str): Name of the parameter
            value(int): Value of the parameter to validate

        Raise:
            TypeError: If value is not an integer
            ValueError: If value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
