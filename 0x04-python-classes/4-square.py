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

    @property
    def size(self):
        """ Is the property of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """" Sets that value of size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Defines Square of area"""

    def area(self, size=0):
        sr_area = self.__size ** 2
        return sr_area

    """ Prints STDOUT  with # """
    def my_print(self):
        if self.__size is 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
