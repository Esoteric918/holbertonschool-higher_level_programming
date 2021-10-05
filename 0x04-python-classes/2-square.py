#!/usr/bin/python3
""" Defines Square by size"""


class Square:
    """ Defines size with varification """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """Defines Square of area"""

    def area(self, size=0):
        sr_area = self.__size ** 2
        return sr_area
