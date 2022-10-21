#!/usr/bin/python3
'''
Module that prints a text with two lines
'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after ., ? and :

    Args:
        text: input text

    Raises:
        TypeError: if text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text[:]

    for i in ".?:":
        list_text = new_text.split(i)
        new_text = ""
        for j in list_text:
            j = j.strip(" ")
            new_text = j + i if new_text is "" else new_text + "\n\n" + j + i

    print(new_text[:-3], end="")
