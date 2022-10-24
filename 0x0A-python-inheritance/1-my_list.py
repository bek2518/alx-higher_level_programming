#!/usr/bin/python3
'''
class Mylist
'''


class MyList(list):
    '''
    Class that inherits attributed of list

    Args:
        list: class
    '''
    def print_sorted(self):

        '''
        function that prints sorted list
        '''
        print(sorted(self))
