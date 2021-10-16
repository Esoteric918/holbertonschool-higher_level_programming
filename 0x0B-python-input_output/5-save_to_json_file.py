#!/usr/bin/python3
"""save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON
    """

    with open(filename) as newFile:
        newFile.write(json.dumps(my_obj))
