#!/usr/bin/python3
"""Takes in letter and sends a POST resquest to url given with
the letter as parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
