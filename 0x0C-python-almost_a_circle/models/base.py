#!/usr/bin/python3
"""base
"""

import json



class Base:
    """Base of the other shapes
    """
    __nb_objects = 0 # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def xyValidator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
    @staticmethod
    def to_json_string(list_dictionaries):
        newLd = []
        if list_dictionaries == None or list_dictionaries == "":
            return newLd
        else:
            newLd = json.dumps(list_dictionaries)
        return newLd

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes to file with JSON string
        """
        with open (cls.__name__ +".json", 'w') as write_file:
            if list_objs == None:
                write_file.write('[]')
            else:
                write_file.write(cls.to_json_string(
                [item.to_dictionary() for item in list_objs]))
