#!/usr/bin/python3
"""Post an email"""


if __name__ == "__main__":
    import sys
    from urllib import request, parse

    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data=data, method='POST')
    with request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
