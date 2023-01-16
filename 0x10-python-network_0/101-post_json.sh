#!/bin/bash
# Makes a POST request with the contents of a file passed as 2nd arg
curl -s "$1" -X POST -f @"$2"
