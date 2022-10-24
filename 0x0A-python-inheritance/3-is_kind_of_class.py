#!/usr/bin/python3
'''
is_kind_of_class function
'''


def is_kind_of_class(obj, a_class):
    '''
    Function that checks if an instance, or an instance of an inherited
    class

    Args:
        obj: object
        a_class: class
    '''

    return (isinstance(obj, a_class))
