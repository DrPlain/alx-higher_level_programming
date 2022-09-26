#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''Returns a list of booleans if the values in a list is a multiple of 2'''

    mult_two = []
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            mult_two.append(True)
        else:
            mult_two.append(False)
    return mult_two
