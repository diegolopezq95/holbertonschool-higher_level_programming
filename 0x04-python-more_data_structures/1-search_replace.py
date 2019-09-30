#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    return [replace if i == search else i for i in new_list]
