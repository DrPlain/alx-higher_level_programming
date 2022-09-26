#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints a list of integers in reverse without .reverse()"""
    if isinstance(my_list, list):
        for i, num in enumerate(my_list):
            i = i + 1
            print("{:d}".format(my_list[-i]))
