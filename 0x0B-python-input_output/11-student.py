#!/usr/bin/python3
"""Student
"""


class Student:
    """Contains student data
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary of Student
        """

        attrString = {}

        if attrs is not None:
            for key in attrs:
                if key in self.__dict__:
                    attrString[key] = self.__dict__[key]
            return attrString
        else:
            return vars(self)

    def reload_from_json(self, json):
        for i in json:
            setattr(self, json[i])
