#!/usr/bin/pyhton3

asci_upper = 91

for number in range(122, 64, -2):
    if (number > 90) & (number < 97):
        continue
    if (asci_upper < 65 | number < 97):
        break
    print("{:c}".format(number), end="")
    asci_upper -= 2
    print("{:c}".format(asci_upper), end="")
