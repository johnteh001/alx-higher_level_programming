#!/usr/bin/python3
"""Search API"""


if __name__ == '__main__':
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except IndexError:
        q = ''
    data = {'q': q}
    response = requests.post(url, data)
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except (ValueError):
        print("Not a valid JSON")
