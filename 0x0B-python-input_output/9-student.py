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

    def to_json(self):
        """returns dictionary representation of the Student instance"""

        return self.__dict__
