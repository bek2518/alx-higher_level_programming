#!/usr/bin/python3
'''
Python script that takes in URL, sends request to URL
and displays value of X-Request-Id variable using requests
'''
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
