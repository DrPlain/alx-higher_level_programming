#!/usr/bin/python3

def list_division(my_list, my_list_2, list_length):
    """Divides two lists element by element"""

    res_list = []

    for i in range(list_length):
        try:
            result = my_list[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            res_list.append(result)
    return res_list
