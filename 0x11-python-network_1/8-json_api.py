#!/usr/bin/python3
'''
Pythons cript that takes in a letter and sends a POST request
with letter as parameter
'''
import requests
import sys

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) == 2:
    value = sys.argv[1]
else:
    value = ""

response = requests.post(url, data={'q': value})
try:
    response.json.loads()
except ValueError:
    print("Not a valid JSON")

with open(response.json) as file:
    data = json.load(file)
    if not data:
        print("No result")

print("[{}] {}".format(response.get('id'), response.get('name')))
