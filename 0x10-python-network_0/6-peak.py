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
        return (max(list[0], list[1]))

    half = len(list) // 2
    return (max(find_peak(list[:half]), find_peak(list[half:])))
