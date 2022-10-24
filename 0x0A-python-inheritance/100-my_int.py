#!/usr/bin/python3
'''
MyInt class
'''


class MyInt(int):
    '''
    Inverts == and != operators
    '''

    def __eq__(self, other):
        '''
        inverts the == operator
        '''

        return (int.__ne__(self, other))

    def __ne__(self, other):
        '''
        Inverts the != operator
        '''

        return (int.__eq__(self, other))
