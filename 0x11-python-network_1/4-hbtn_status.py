#!/usr/bin/python3
"""Using requests"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", response.text.__class__)
    print("\t- content:", response.text)
