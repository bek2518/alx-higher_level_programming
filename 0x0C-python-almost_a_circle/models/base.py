#!/usr/bin/python3
'''
Create a Base class
'''
import json
import csv


class Base:
    '''
    Base class for others
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Intitalization

        Args:
            id: id
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Static method that changes to a json string

        Args:
            list_dictionaries: list of dictionary
        '''

        if list_dictionaries is None:
            return ('[]')
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Class method that saves json representation into a file

        Args:
            cls: class
            list_objs: list of objects
        '''

        try:
            json_string = cls.to_json_string(
                [x.to_dictionary() for x in list_objs])
        except BaseException:
            json_string = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns list of json string representation of json_string '''

        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attr set '''
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        if cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                dict_list = cls.from_json_string(f.read())
            return ([cls.create(**x) for x in dict_list])
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of rectangles or squares in csv.
        Args:
            cls (any): class.
            list_objs (list): objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                for i in list_objs:
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of rectangles or squares in csv.
        Args:
            cls (any): class.
        """
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)
