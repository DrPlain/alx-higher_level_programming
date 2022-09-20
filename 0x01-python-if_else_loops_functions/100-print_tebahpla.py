#!/usr/bin/python3

asci_upper = 91

for number in range(122, 96, -2):
    asci_upper -= 2
    print("{:c}{:c}".format(number, asci_upper), end="")
