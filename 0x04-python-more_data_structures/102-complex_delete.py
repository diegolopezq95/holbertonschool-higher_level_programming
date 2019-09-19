#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = a_dictionary.copy()
    if value:
        for key, values in new_dictionary.items():
            if a_dictionary[key] == value:
                del a_dictionary[key]
        return a_dictionary
    else:
        return new_dictionary
