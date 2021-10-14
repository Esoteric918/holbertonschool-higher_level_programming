#!/usr/bin/python3
""" Rectangle inherited from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
"""Defines the Rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", height)
        super().integer_validator("height", width)
        self.__width = width
        self.__height = height

    def area(self):
        area = self.__width * self.__height
        return area

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
