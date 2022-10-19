#!/usr/bin/python3
'''
Class with no class of object attribute, that prevents the user
from dynamically creating new instance
'''


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        '''
        initialize
        '''

        pass
