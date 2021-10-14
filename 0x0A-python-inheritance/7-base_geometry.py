#!/usr/bin/python3
""" Set class BaseGeometry
"""


class BaseGeometry:
    """Contains functions area(), integer_validator()
    """

    def area(self):
        """ raises Exception
        """
        raise Exception("area() is not implemented")

    """function validates value
            """

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
