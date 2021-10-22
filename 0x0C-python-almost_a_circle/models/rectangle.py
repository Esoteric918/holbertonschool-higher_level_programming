#!/usr/bin/python3
"""rectangle inherits form Base
"""
from models.base import Base


class Rectangle(Base):
    """ rectangle Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init method for class'''
        super().__init__(id)

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.xyValidator("x", x)
        self.__x = x
        self.xyValidator("y", y)
        self.__y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''widht setter'''
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.xyValidator("x", value)
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.xyValidator("y", value)
        self.__y = value

    def area(self):
        '''returns area of rectangle'''
        area = self.__height * self.__width
        return area

    def display(self):
        '''prints a rep of the rec in stdout
        using #'''
        for row in range(self.__y):
            print("")
        for row in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width)

    def __str__(self):
        '''str representation of obj'''
        return "[Rectangle] ({}) {}/{} {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''Set values of self based on args or kwargs'''
        Attr = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            if i == 0:
                self.__dict__['id'] = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
         '''Return dict of obj values'''
        newDict = {}

        newDict['id'] = self.id
        newDict['width'] = self.width
        newDict['height'] = self.height
        newDict['x'] = self.x
        newDict['y'] = self.__y
        return newDict
