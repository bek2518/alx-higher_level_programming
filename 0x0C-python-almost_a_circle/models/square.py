#!/usr/bin/python3
'''
Create Square class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class that inherits from Rectangle class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initialize

        Args:
            size: width/ height of square
            x: axis x
            y: axis y
            id: id
        '''

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''
        Getter for size
        '''

        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter for size

        Args:
            size: size of square
        '''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value

    @property
    def width(self):
        '''
        Getter for width
        '''

        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for width

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
        Setter for y

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
        Calculates the area of a square
        '''

        return (self.size * self.size)

    def display(self):
        '''
        Displays the square
        '''

        for j in range(self.y):
            print()
        for i in range(self.__height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        '''
        Overwrites the __str__
        '''

        return (("[Square] ({:d}) {:d}/{:d} - {:d}")
                .format(self.id, self.x, self.y, self.width or self.height))

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute

        Args:
            *args: non key worded
            **kwargs: key-worded
        '''

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'size' in kwargs.keys():
                self.size = kwargs['size']
            if 'x' in kwargs.keys():
                self.x = kwargs['x']
            if 'y' in kwargs.keys():
                self.y = kwargs['y']

    def to_dictionary(self):
        '''
        Returns dictionary representation of square
        '''

        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
