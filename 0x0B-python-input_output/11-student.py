#!/usr/bin/python3
""" studen module class"""


class Student:
    """Class student """

    def __init__(self, first_name, last_name, age):
        """Initializes student

        Args:
            first_name(str): first name of student
            last_name(str):last name of student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of the Student instance"""

        if attrs is not None and len(attrs) != 0:
            new_dict = {i: self.__dict__[i] for i in
                        self.__dict__.keys() & attrs}
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces the attritues of the instance. """

        for k, v in json.items():
            self.__setattr__(k, v)
