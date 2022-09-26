#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Finds the biggest integer of a list without using max function'''
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return None

        max_num = my_list[0]
        for i, num in enumerate(my_list):
            if my_list[i] > max_num:
                max_num = my_list[i]
        return max_num
