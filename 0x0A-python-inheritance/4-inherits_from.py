#!/usr/bin/python3
"""inherits_form
"""


def inherits_from(obj, a_class):
    """ Returns TRUE if form the same subclass
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
