#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''Replaces an element in a list without modifying the original list'''

    if isinstance(my_list, list):
        if (idx < 0) | (idx >= len(my_list)):
            return my_list
        newList = list(my_list)
        newList[idx] = element
        return newList
