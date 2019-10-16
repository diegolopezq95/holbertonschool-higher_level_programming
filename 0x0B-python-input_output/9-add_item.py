#!/usr/bin/python3
""" This script adds all arguments to a Python list,
 and then save them to a file
"""


import os
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if len(argv) > 0 and os.path.exists("add_item.json"):
    obj = load_from_json_file("add_item.json")
else:
    obj = []
for i in argv[1:]:
    obj.append(i)
save_to_json_file(obj, "add_item.json")
