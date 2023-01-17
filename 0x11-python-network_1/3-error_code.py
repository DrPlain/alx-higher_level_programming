#!/usr/bin/python3
""" Sends a request to an url and displays the body of response """


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
