#!/usr/bin/python3
"""Base module"""

import json


class Base:
    """Base class

        Attributes:
            __nb_objects(int): number of objects

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__intializes the class.

        Args:
            id(int): public instance attribute.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Creates JSON string representation of the dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """The method writes the JSON string representation of
        list_objs to a file.

        Args:
            list_objs(base obj): A list of instances inheriting Base.

        """
        dictionary = []
        filename = cls.__name__ + '.json'
        if list_objs is not None and len(list_objs) > 0:
            for i in list_objs:
                i = i.to_dictionary()
                json_d = json.loads(cls.to_json_string(i))
                dictionary.append(json_d)
        with open(filename, "w") as f:
            json.dump(dictionary, f)

    def from_json_string(json_string):
        """Function returns a list from the JSON string"""

        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy = Rectangle(2, 3)
        elif cls.__name__ == "Square":
            dummy = Square(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Function returns a list of instances."""

        dictionary = {}
        new_list = []
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
            json_list = cls.from_json_string(json_string)
            for i in json_list:
                dummy = cls.create(**i)
                new_list.append(dummy)
            return new_list
        except:
            return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes to CSV file"""
        import csv
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            csv_obj = csv.writer(csvfile)
            if list_objs is not None:
                for i in list_objs:
                    if filename == "Rectangle.csv":
                        csv_obj.writerow([i.id, i.width, i.height, i.x, i.y])
                    elif filename == "Square.csv":
                        csv_obj.writerow([i.id, i.size, i.x, i.y])
            else:
                csv_obj.writerow('[]')

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from CSV file"""
        import csv

        filename = cls.__name__+'.csv'
        with open(filename, 'r') as csvfile:
            if filename == "Rectangle.csv":
                read_obj = csv.DictReader(csvfile, fieldnames={'id', 'width',
                                                               'height', 'x',
                                                               'y'})
            if filename == "Square.csv":
                read_obj = csv.DictReader(csvfile, fieldnames={'id', 'size',
                                                               'x', 'y'})
            instance_list = []
            for obj in read_obj:
                obj = {x: int(y) for x, y in obj.items()}
                instance = cls.create(**obj)
                instance_list.append(instance)
        return instance_list
