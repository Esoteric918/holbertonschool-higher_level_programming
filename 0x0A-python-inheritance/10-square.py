#!/usr/bin/python3
""" Square inherits Rectangle which inherits from BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square data that inherits from Rectangle
       init `size` twice because width and height are same in squares
    """

    def __init__(self, size):
        super().integer_validator(size, size)
        super().__init__(size, size)
        self.size = size

    def area(self):

        return self.size * self.size
