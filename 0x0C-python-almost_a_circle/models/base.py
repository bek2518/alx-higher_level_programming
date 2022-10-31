#!/usr/bin/python3
'''
Create a Base class
'''
import json


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
            return ([])
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

    @classmethod
    def from_json_string(json_string):
        '''
        Returns list of json string representation of json_string
        '''

        if json_string is None or len(json_string) == 0:
            return ([])
        else
            return json.loads(json_string)
