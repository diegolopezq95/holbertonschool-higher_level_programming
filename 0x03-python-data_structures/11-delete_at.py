#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not len(my_list):
        return None
    else:
        for i in range(len(my_list)):
            if idx < 0 or idx > len(my_list) - 1:
                return my_list
                if i == idx:
                    my_list.remove(idx)
                else:
                    continue
                    new_list = my_list.copy()
        return new_list
