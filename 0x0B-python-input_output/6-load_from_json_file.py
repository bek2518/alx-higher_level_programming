#!/usr/bin/python3
'''
load_from_json_file function
'''
import json


def load_from_json_file(filename):
    '''
    Function that creates an object from JSON file

    Args:
        my_obj: object (string)
        filename: file name
    '''

    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f)
