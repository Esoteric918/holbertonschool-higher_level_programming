#!/usr/bin/python3
"""load_from_json_file
"""
import json

def load_from_json_file(filename):
    """ creates an Object from a “JSON file”
    """
    with open(filename) as readFile:
        return json.loads(readFile.read())
