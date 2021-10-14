#!/usr/bin/python3
""" Rectangle inherited from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        super().integer_validator("width", height)
        super().integer_validator("height", width)
        self.__width = width
        self.__height = height

    def area(self):
        """Determins area
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Magic Trick !
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
