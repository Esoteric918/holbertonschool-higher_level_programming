#!/usr/bin/python3
"""Error codes"""
import urllib.request
import sys


def errorCode():
    """Error code check"""
    url = sys.argv[1]
    req =urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:".format(e.code))

if __name__ == "__main__":
    errorCode()
