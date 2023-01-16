#!/bin/bash
# Bash script that takes in URL, sends request to that URL and displays the size of bosy of the response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2