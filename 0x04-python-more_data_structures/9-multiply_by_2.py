#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    list_dir = list(new_dictionary.keys())
    for i in list_dir:
        new_dictionary[i] *= 2
    return (new_dictionary)
