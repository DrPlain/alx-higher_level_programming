#!/usr/bin/python3
""" Displays a header value """
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers['X-Request-Id'])
