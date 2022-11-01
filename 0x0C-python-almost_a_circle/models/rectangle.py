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
        '''
        Initialization

        Args:
            width: width of rectangle
            height: height of rectangle
            x: axis x
            y: axis y
            id: id
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
        getter for width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter for width

        Args:
            value: value
        '''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Getter for height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for height

        Args:
            value: value
        '''

        if not isinstance(value,  int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Getter for x
        '''

        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for x

        Args:
            value: value
        '''

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Getter for y
        '''

        return self.__y

    @y.setter
    def y(self, value):

        '''
        setter for y

        Args:
            value: value
        '''

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Public instance that calculates the area
        '''

        return (self.width * self.height)

    def display(self):

        '''
        Public instance that displays the rectangle
        '''

        for j in range(self.y):
            print()
        for i in range(self.__height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        '''
        Overrides the __str__ method
        '''

        return (("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}")
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute

        Args:
            *args: non-keyword variable
            **kwargs: key-worded variable
        '''

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'width' in kwargs.keys():
                self.width = kwargs['width']
            if 'height' in kwargs.keys():
                self.height = kwargs['height']
            if 'x' in kwargs.keys():
                self.x = kwargs['x']
            if 'y' in kwargs.keys():
                self.y = kwargs['y']

    def to_dictionary(self):
        '''
        Returns dictionary representation
        '''

        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
