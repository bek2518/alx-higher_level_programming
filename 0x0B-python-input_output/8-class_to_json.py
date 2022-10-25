#!/usr/bin/pyhton3
'''
class_to_json function
'''


def class_to_json(obj):
    '''
    Function that returns the dictionary description

    Args:
        obj: object
    '''

    return obj.__dict__
