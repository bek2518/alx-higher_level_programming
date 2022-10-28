#!/usr/bin/python3
'''
Create Rectangle class that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class that inherits from base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value,  int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        for j in range(self.y):
            print()
        for i in range(self.__height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        return (("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}")
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.weigth = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]
