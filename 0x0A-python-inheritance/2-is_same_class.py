#!/usr/bin/python3
'''
is_same_class function
'''


def is_same_class(obj, a_class):
    '''
    Function that checks if object is exactly an instance of specified class

    Args:
        obj: object
        a_class: class type
    '''
    return (type(obj) is a_class)
