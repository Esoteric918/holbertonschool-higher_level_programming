#!/usr/bin/python3
""" define class MyList that inherits from list
    """


class MyList(list):
    """contains list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints self in sorted format
        """
        print(sorted(self))
