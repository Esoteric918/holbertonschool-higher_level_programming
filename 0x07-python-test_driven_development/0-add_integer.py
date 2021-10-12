#!/usr/bin/python3

"""
function that adds 2 integers
Returns an integer: addition of a and b
"""


def add_integer(a, b=98):
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
