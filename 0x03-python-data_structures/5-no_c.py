#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    new_string = my_string.copy()
    for i in (new_string):
        if i == 'c':
            new_string.remove('c')
        elif i == 'C':
            new_string.remove('C')
        else:
            continue
    return''.join(new_string)
