#!/usr/bin/python3
'''
append_after function
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Function that inserts a line of text to a file after
    each line with a specific string

    Args:
        filename: filename
        search_string: string to be searched
        new_string: string to append
    '''

    output = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            output = output + line
            if search_string in line:
                output = output + new_string

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)
