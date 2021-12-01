#!/usr/bin/python3
"""POST an email #0"""
import urllib.request
import urllib.parse
import sys


def postIt():
    """POST email"""
    em = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(em)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode("utf-8"))


if __name__ == "__main__":
    postIt()
