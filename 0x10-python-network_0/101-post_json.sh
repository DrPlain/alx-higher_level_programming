#!/bin/bash
# Makes a POST request with the contents of a file passed as 2nd arg
curl -s -H "content-type:application/json" -X POST -d @"$2" "$1"
