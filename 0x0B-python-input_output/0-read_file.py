#!/usr/bin/python3
"""this function reads a file """


def read_file(filename=""):
    with open(filename, encoding='utf-8') as readFile:
        print(readFile.read(), end="")
