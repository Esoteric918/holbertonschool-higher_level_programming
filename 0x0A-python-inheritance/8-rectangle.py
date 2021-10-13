#!/usr/bin/python3
""" Rectangle inherited from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        super().integer_validator(width, height)
        super().integer_validator(height, width)
        self.width = width
        self.height = height

