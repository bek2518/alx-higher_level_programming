#!/usr/bin/pyhton3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in range(0, len(my_list)):
        print("{}".format(my_list[i]))
