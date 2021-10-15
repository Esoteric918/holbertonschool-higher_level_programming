#!/usr/bin/python3
""" Writes to a file"""


def write_file(filename="", text=""):
    """ Writes to a file makes file if not there
    rewrites if text is there"""

    with open(filename, 'w', encoding='utf-8') as writeFile:
        writeFile.write(text)
        return len(text)