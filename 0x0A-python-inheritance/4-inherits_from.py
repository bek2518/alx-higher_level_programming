#!/usr/bin/python3
'''
inherits_from dunction
'''


def inherits_from(obj, a_class):
    '''
    Function that checks if obj is an instance of a class that
    inherited from a_class

    Args:
        obj: objcet
        a_class: class
    '''

    if type(obj) == a_class:
        return False
    return (issubclass(type(obj), a_class))
