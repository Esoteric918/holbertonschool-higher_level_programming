#!/usr/bin/python3
"""POST an email #0"""
import urllib.request
import urllib.parse
import sys

def postIt():
    em = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(em)
    data = data.encode("utf-8")
    request = urllib.request.urlopen(sys.argv[1], data)

    with urllib.request.urlopen(request) as response:
        header = response.info()
        print(data.decode("utf-8"))

if __name__ == "__main__":
    postIt()
