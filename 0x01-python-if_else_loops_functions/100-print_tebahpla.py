#!/usr/bin/python3

asci_upper = 91

for number in range(122, 96, -2):
    print("{:c}".format(number), end="")
    asci_upper -= 2
    print("{:c}".format(asci_upper), end="")
