#!/usr/bin/python3
"""rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
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
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.xyValidator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.xyValidator("y", value)
        self.__y = value

    # area of the rectangle

    def area(self):
        area = self.__height * self.__width
        return area

    # displays rectagle with '#'

    def display(self):
        for row in range(self.__y):
            print("")
        for row in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width)

    # Overrides string rep

    def __str__(self):
        return "[Rectangle] ({}) {}/{} {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    # assigns an argument to each attribute

    def update(self, *args, **kwargs):
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
        newDict = {}

        newDict['id'] = self.id
        newDict['width'] = self.width
        newDict['height'] = self.height
        newDict['x'] = self.x
        newDict['y'] = self.__y
        return newDict
