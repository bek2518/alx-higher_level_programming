#!/usr/bin/python3
'''
Defining class Square
'''


class Square:
    '''
    Square class with private instance attribute size
    '''
    def __init__(self, size=0):
        '''
        Args:
            size: size of square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def get(self):
        '''
        Method to get the size
        '''
        return self.__size

    def set(self, value):
        '''
        Set the value
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value

    def area(self):
        area_size = self.__size * self.__size
        return area_size

    def my_print(self):
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
