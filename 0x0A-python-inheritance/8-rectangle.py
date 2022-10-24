#!/usr/bin/python3
'''
BaseGeometry class
'''


class BaseGeometry:
    '''
    Base class
    '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectange(BaseGeometry):
    '''
    Rectangle class that inherits from BaseGeometry
    '''

    def __init__(self, width, height)
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
        self.__width = width
        self.__height = height
