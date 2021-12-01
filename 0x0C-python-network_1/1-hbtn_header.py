#!/usr/bin/python3
"""Response header value"""
import urllib.request
import sys


def getHead():
    """ takes in a URL, sends a request to the URL and displays
        the value of the X-Request-Id variable
        found in the header of the response."""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header['X-Request-Id'])

if __name__ == "__main__":
    getHead()
