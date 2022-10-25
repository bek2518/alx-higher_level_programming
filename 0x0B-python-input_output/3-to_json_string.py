#!/usr/bin/python3
'''
to_json_string function
'''


import json

def to_json_string(my_obj):
    '''
    Returns the JSON representation of an object (string)

    Args:
        my_object: object (string)
    '''

    return json.dump(my_obj)
