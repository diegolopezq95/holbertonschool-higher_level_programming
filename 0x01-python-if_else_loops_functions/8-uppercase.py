#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if str[i].islower():        
            c = c - 32
        print('{}'.format(chr(c)), end="")
    print()
