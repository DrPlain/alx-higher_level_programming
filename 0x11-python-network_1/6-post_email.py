#!/usr/bin/python3
""" Takes in a url and email and sends a POST request to url
"""
import requests
from sys import argv


if __name__ == "__main__":
    value = {"email": argv[2]}
    r = requests.post(argv[1], data=value)
    print(r.text)
