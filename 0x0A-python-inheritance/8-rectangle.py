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
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


'''
Rectangle class
'''


class Rectange(BaseGeometry):
    '''
    Rectangle class that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        '''
        Function that instantiates width and height

        Args:
            width: width
            height: height
        '''

        self.__width = width
        self.__height = heigh
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
