#!/usr/bin/python3
'''
append_write function
'''


def append_write(filename="", text=""):
    '''
    Function that appends a string at the end of a text file

    Args:
        filename: file name
        text: text to be written
    '''

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
