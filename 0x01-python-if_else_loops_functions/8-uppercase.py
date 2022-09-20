#!/usr/bin/python3

def uppercase(str):

    for i in range(len(str)):
        asci = ord(str[i])
        if (asci >= 97) & (asci <= 122):
            print("{:c}".format(asci - 32),
                  end="" if (i < len(str) - 1) else "\n")
        else:
            print(str[i], end="" if (i < len(str) - 1) else "\n")
