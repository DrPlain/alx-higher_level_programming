#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers, prints result and handles exceptions"""

    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
