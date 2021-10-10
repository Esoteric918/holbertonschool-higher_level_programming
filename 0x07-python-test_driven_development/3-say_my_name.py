#!/usr/bin/python
""" say_my_name prints the parameters
first_name followed by last_name
last_name is defaulted to an empty string
"""


def say_my_name(first_name, last_name=""):
    """ My name is <first name> <last name>
    checks if <first name> is str
    checks if <last name> is str
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
