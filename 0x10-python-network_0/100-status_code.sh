#!/bin/bash
# Sends a request to a URL passes and displays only the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
