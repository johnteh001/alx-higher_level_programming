#!/usr/bin/python3
"""GitHub API"""


if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(username, token))
    print(response.json().get('id'))
