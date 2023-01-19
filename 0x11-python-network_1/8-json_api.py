#!/usr/bin/python3
'''
Pythons cript that takes in a letter and sends a POST request
with letter as parameter
'''
import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) >= 2:
        value = sys.argv[1]
    else:
        value = ""

    response = requests.post(url, data={'q': value})
    try:
        if response.json == {} or not response.json.get('id') or\
                        not not response.json.get('name'):
            print("No result")

    except:
        print("Not a valid JSON")

    else:
        response = response.json()
        print("[{}] {}".format(response.get('id'), response.get('name')))
