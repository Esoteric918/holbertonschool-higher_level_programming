#!/usr/bin/python3
"""base class for geometry classes
"""

import json


class Base:
    """Base class for classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        '''Iniitialization Method'''
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        '''Value verification for width & height'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def xyValidator(self, name, value):
        '''Value verification for x & y'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation
        """
        newLd = []
        if list_dictionaries is None or list_dictionaries == "":
            return ("[]")
        else:
            newLd = json.dumps(list_dictionaries)
        return newLd

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes to file with JSON string
        """
        with open(cls.__name__ + ".json", 'w') as write_file:
            if list_objs is None:
                write_file.write('[]')
            else:
                write_file.write(cls.to_json_string(
                    [item.to_dictionary() for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns JSON strings in list
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''instantiate a cls obj based on kwargs(**dictionary)'''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''load geometric objects from associated csv files'''
        try:
            with open(cls.__name__ + '.json', 'r') as readFile:
                return [cls.create(**i)
                        for i in cls.from_json_string(readFile.read())]
        except:
            return []
