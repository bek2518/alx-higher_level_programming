#!/usr/bin/python3
'''
Rectangle class definition
'''


class Rectangle:
    '''
    Initiation of Rectangle class
    '''
    def __init__(self, width=0, height=0):
        '''
        Args:
            width: width of the rectangle
            height: height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Retreives width
        '''

        return self.__width

    @width.setter
    def width(self, value):
        '''
        sets width

        Args:
            value: value to set width to
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Retreives height
        '''

        return self.__height

    @height.setter
    def height(self, value):
        '''
        Sets height

        Args:
            value: value to set height to
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''
        Calculates area of a rectangle
        Return:
            area of the rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        Calculates the perimeter of a rectangle
        Return:
            0 if either width or height is zero
            else the rectangle perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
