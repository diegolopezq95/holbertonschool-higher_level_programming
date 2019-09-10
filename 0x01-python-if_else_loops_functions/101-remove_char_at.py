#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if n >= 0 and n < len(str):
            strcpy = str[:n] + str[n + 1:]
            return strcpy
        else:
            return str
