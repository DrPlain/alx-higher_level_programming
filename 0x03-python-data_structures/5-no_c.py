#!/usr/bin/python3

def no_c(my_string):
    '''Removes all characters c and C from a string'''

    newStr = ""
    for character in my_string:
        if (character == 'c') or (character == 'C'):
            continue
        newStr += character
    return newStr
