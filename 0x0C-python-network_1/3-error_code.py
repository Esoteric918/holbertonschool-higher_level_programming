#!/usr/bin/python3
"""Error codes"""
from urllib import error, request, parse
from sys import argv
import urllib


def errorCode():
    """Error code check"""
    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:".format(e.code))

if __name__ == "__main__":
    errorCode()
