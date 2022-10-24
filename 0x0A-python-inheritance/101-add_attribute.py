#!/usr/bin/python3
'''
Creates a function that adds new attribute
'''


def add_attribute(obj, name. value):
    '''
    Function that adds new attribute to an object if possible

    Args:
        obj: object
        name: name of attribite
        value: value of attribute
    Raises:
        TypeError: if attribute cannot be added
    '''

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
