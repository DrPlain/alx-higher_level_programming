#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    '''Console calculator that handles basic operations'''

    count = len(argv) - 1
    result = 0

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] == '+':
        result = add(int(argv[1]), int(argv[3]))
    elif argv[2] == '-':
        result = sub(int(argv[1]), int(argv[3]))
    elif argv[2] == '*':
        result = mul(int(argv[1]), int(argv[3]))
    elif argv[2] == '/':
        result = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))


if __name__ == "__main__":
    main()
