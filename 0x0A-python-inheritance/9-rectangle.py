#!/usr/bin/python3
'''
This module creates a class that inherits BaseGeometry class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Implements a rectangle
    '''

    def __init__(self, width, height):
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Area of the rectangle
        '''

        return self.__width * self.__height

    def __str__(self):
        '''
        Prints out a string
        '''

        return ("[Rectangle {}/{}]".format(self.__width, self.__height))
