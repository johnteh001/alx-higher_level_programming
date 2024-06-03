#!/usr/bin/python3
"""Handling Error Code"""


if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib.error import HTTPError

    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
