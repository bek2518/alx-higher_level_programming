#!/usr/bin/python3
'''
from_json_string function
'''
import json


def from_json_string(my_obj):
    '''
    Returns the object represented by JSON

    Args:
        my_object: object (string)
    '''

    return json.loads(my_obj)
