#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(name, a_dictionary[name]))
     for name in sorted(a_dictionary)]
