#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Finds the biggest integer of a list without using max function'''

    if isinstance(my_list, list):
        if my_list == []:
            return None
        for i, num in enumerate(my_list):
            if (i+1) < len(my_list):
                if my_list[i] < my_list[i+1]:
                    my_list[i] = my_list[i+1]
        return my_list[0]
