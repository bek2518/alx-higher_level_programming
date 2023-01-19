#!/usr/bin/python3
'''
Function that finds a peak in a list of unsorted integers
'''


def find_peak(list_of_integers):
    '''
    Function that sorts through a list in recursive manner and finds the peak
    '''
    list = list_of_integers

    if len(list) == 0:
        return

    if len(list) == 1:
        return list[0]

    elif len(list) == 2:
        a = list[0]
        b = list[1]
        if a <= b:
            return b
        else:
            return a

    half = len(list) // 2

    c = find_peak(list[:half])
    d = find_peak(list[half:])
    if c <= d:
        return d
    else:
        return c
