#!/usr/bin/python3
'''
load_from_json_file function
'''
import json


def load_from_json_file(my_obj, filename):
    '''
    Function that creates an object from JSON file

    Args:
        my_obj: object (string)
        filename: file name
    '''

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.loads(my_obj))
