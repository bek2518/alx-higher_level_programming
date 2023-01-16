#!/bin/bash
# Bash script that takes URL as an argument and sends GET request to the URL displays the body of the response
curl -sX GET -H "X-School-User-ID: 98" "$1"
