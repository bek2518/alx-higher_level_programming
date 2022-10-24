#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


'''
Rectangle class
'''


class Rectange(BaseGeometry):
    '''
    Rectangle class that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        '''
        Instantiation width and height

        Args:
            width: width
            height: height
        '''
        self.__width = width
        self.__height = heigh
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
