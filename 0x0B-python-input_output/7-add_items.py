#!/usr/bin/python3
'''
add_item
'''


import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('7-load_from_json_file').load_from_json_file

if os.path.isfile("add_item.json"):
    new_file = load_from_json_file("add_item.json")
else:
    new_file = []
new_file.extend(sys.argv[1:])
save_to_json_file(new_file, "add_item.json")
