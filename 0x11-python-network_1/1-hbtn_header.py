#!/usr/bin/python3
"""Status module: fetches url"""


if __name__ == "__main__":
    import sys
    from urllib import request

    req = sys.argv[1]
    with request.urlopen(req) as response:
        page = response.getheader("X-Request-Id")
        print(page)
