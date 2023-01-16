#!/bin/bash
# Takes an url, sends a GET request & displays the body of response
curl -sfL "$1" -X GET
