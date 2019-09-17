#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    for i in my_string:
        new_string = my_string.copy()
        if i == 'c':
            new_string.remove('c')
            return ''.join(new_string)
        elif i == 'C':
            new_string.remove('C')
            return ''.join(new_string)
        else:
            continue
