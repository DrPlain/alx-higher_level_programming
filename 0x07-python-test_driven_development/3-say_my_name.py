#!/usr/bin/python3
"""Module for printing name"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name(str): First name
        last_name(str): Last name, optional
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    first_name = first_name.lower().title().strip()
    last_name = last_name.lower().title().strip()
    print(f"My name is {first_name} {last_name}")
