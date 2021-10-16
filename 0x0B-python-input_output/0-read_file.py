#!/usr/bin/python3
"""this function reads a file """


def read_file(filename=""):
    """reads file and prints to stdout
    """

    with open(filename, encoding='utf-8') as readFile:
        print(readFile.read(), end="")
