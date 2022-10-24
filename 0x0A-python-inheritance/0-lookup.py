#!/usr/bin/python3
def lookup(obj):
    '''
    Function that returns the list of available attribues
    and methods of an object

    Args:
        obj: instance of the class
    '''

    return dir(obj)
