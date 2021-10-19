#!/usr/bin/python3
"""
Square
"""
from models.rectangle import Rectangle

class Square(Rectangle):


    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        Attr = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        newDict = {}

        newDict['id'] = self.id
        newDict['size'] = self.size
        newDict['x'] = self.x
        newDict['y'] = self.y
        return newDict
