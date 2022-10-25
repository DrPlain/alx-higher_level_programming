#!/usr/bin/python3
"""contains the function read_file(filename='')"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename(str): Name of file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
