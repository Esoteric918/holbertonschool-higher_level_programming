#!/usr/bin/python3
""" Set class BaseGeometry
"""


class BaseGeometry:
    """ raises Exception
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function validates value
        """

        if type(value) is not int:
            raise TypeError(name, "must be an integer")
        if value <= 0:
            raise ValueError(name, "must be greater than 0")
