#!/usr/bin/python3
'''
Module that adds all arguments to python list
and save them to file
'''


import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('7-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)
save_to_json_file(new_file, "add_item.json")
