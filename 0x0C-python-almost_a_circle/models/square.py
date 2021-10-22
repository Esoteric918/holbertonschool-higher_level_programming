#!/usr/bin/python3
"""
Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square inherits Base"""

    def __init__(self, size, x=0, y=0, id=None):
        '''init method for square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of object'''
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''Size setter with validation, using inherited width & height'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Updates attributes in specific order for args,
        and with key:val pairs for kwargs
        '''
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
        '''String version of JSON interpretation'''
        newDict = {}

        newDict['id'] = self.id
        newDict['size'] = self.size
        newDict['x'] = self.x
        newDict['y'] = self.y
        return newDict
