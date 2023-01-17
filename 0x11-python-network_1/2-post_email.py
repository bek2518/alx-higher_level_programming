#!/usr/bin/python3
'''
Python script that takes in URL and email, sends POSt request to the URL
with the email parameter and display body of the response
'''
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email_address = sys.argv[2]
    value = {'email': email_address}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read())
