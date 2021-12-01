#!/usr/bin/python3
"""whats my status? #0"""
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as resp:
        html = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
