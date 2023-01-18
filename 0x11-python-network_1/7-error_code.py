#!/usr/bin/python3
""" Sends a request to a url and displays the body of response
- If status code >= 400 print Error code: <status code>
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
