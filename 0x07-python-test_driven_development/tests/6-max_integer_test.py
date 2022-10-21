#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    '''
    Class definition for max integer
    '''

    def max_int_test(self):
        '''
        tests list of integers
        '''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def max_int_test_empty(self):
        '''
        tests an empty list
        '''
        self.assertEqual(max_integer([]), None)

    def max_int_test_neg(self):
        '''
        tests list with a negative integer
        '''
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def max_int_test_one(self):
        '''
        tests list with only one integer
        '''
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
