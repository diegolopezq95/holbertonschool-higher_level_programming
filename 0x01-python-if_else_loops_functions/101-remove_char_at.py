#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    for i in range(len(str)):
        strcpy = str[:n] + str[n + 1:]
        if n >= 0 and n < len(str):
            return strcpy
        else:
            return str
