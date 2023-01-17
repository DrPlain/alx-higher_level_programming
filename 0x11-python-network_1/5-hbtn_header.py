#!/usr/bin/python3
""" Displays a header value """
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers['X-Request-Id'])
