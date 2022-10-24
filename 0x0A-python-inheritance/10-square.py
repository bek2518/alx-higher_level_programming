#!/usr/bin/python3
'''
This module creates a class that inherits Rectangle class
'''


Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    '''
    Implements a square
    '''

    def __init__(self, size):
        self.__size = super().integer_validator('size', size)
        self.__size = size
        super().__init__(size,size)
    
    def area(self):
        '''
        Returns area of the square
        '''

        return self.__size * self.__size
