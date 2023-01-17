#!/usr/bin/python3
'''
Python script that takes in URL, sends a request to the URL
and displays the body, and Error code if status code >= 400
'''
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
