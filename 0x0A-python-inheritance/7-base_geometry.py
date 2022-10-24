#!/usr/bin/python3
'''
BaseGeometry class
'''


class BaseGeometry:
    '''
    Base class
    '''

    def area(self):
        '''
        Function that raises an exception
        '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Function that validates value

        Args:
            name: string name
            value:value
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
