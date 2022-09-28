#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for v, i in sorted(a_dictionary.items()):
        print('{}: {}'.format(v, i))
