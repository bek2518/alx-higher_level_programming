#!/usr/bin/python3
'''
Python script that takes GitHub credentials and uses Github API to display id
'''
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))
    print(response.json().get('id'))
