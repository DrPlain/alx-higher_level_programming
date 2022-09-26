#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints a list of integers in reverse"""

    for i, num in enumerate(my_list):
        i = i + 1
        print(my_list[-i])
