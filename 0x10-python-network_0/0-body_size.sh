#!/usr/bin/bash
# A script that takes in a url, sends a request to that URL
# and displays the size of the body of the response
# -s == silent mode, -I == display only head

curl -sI "$1" | grep -i Content-Length | cut -d ':' -f2
