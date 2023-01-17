#!/usr/bin/python3
'''
Python script that takes lists 10 commits oldest to newest of
repository and user given as arguments
'''
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)

    response = requests.get(url)
    responses = response.json()
    for list in responses[:10]:
        print("{}: {}".format(list.get('sha'),
                              list.get('commit').get('author').get('name')))
