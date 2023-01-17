#!/usr/bin/python3
""" Displays a header value """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.get('X-Request-Id'))
