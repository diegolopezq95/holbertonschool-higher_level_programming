#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    for i in range(len(str)):
        if n >= 0:
            strcpy = str[:n] + str[n + 1:]
            return strcpy
        else:
            return str
