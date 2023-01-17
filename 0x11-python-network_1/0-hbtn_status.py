#!/usr/bin/python3
""" Fetches a given url using urlib """
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:\n     - type: {}\n     - content: {}\n\
     - utf8 content: OK".format(
            type(content), content))
