#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dir = {
        'I' : 1,
        'IV': 4,
        'V' : 5,
        'IX': 9,
        'X' : 10,
        'XL': 40,
        'L' : 50,
        'XC': 90,
        'C' : 100,
        'CD' : 400,
        'D' : 500,
        'CM' : 900,
        'M' : 1000
    }
    num = 0
    i = 0
    while i < len(roman_string):
        if roman_string[i: i + 2] in my_dir:
            num += my_dir[roman_string[i: i + 2]]
            i += 2
        else:
            num += my_dir[roman_string[i]]
            i += 1
    return num
