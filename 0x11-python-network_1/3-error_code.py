#!/usr/bin/python3
""" Sends a request to an url and displays the body of response """
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
