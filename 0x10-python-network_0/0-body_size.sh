#!/bin/bash
# Takes an url, sends a request & displays the content-length
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
