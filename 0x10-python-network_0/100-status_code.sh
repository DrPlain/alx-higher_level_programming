#!/bin/bash
# Get status code without using pipe, >, ;, &&,
curl -s "$1" -o /dev/null -w "%{response_code}"
