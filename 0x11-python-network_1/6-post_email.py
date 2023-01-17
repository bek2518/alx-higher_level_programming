#!/usr/bin/python3
'''
Python script that takes in URL and email, sends POSt request to the URL
with the email parameter and display body of the response
'''
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email_address = sys.argv[2]
    response = requests.post(url, data={'email': email_address})
    print(response.text)
