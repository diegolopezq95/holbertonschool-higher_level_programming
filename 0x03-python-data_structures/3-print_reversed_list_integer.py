#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if my_list == []:
            return None
        else:
            my_list.reverse()
            print("{:d}".format(my_list[i]))
