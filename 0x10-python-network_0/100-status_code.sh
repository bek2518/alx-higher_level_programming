#!/bin/bash
# Sends a request to a URL passes and displays only the status code of the response
curl -sI "$1" | grep HTTP | cut -d ' ' -f2
