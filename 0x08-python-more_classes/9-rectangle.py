#!/usr/bin/python3
'''
Rectangle class definition
'''


class Rectangle:
    '''
    Initiation of Rectangle class
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Args:
            width: width of the rectangle
            height: height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        '''
        prints the rectangle using print_symbol
        '''
        rec = ""
        if self.width == 0 or self.height == 0:
            return rec
        else:
            for i in range(self.height):
                rec = rec + (str(self.print_symbol) * self.width) + "\n"
        return rec[:-1]

    def __repr__(self):
        '''
        return string representation
        '''
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        '''
        prints message when an instance deleted
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        Compares and returns the biggest rectangle on area

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    
    @classmethod
    def square(cls, size=0):
        '''
        Returns new rectangle with width == height == size

        Args:
            cls: new rectangle class
            size: width and height of rectangle
        '''
        return cls(size, size)
