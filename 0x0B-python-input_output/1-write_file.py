#!/usr/bin/python3
'''
write_file function
'''


def write_file(filename="", text=""):
    '''
    Function that writes a string to a text file

    Args:
        filename: file name
        text: text to be written
    '''

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
