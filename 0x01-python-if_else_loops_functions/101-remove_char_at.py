#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    if n >= 0 and n < len(str):
        strcpy = str[:n] + str[n + 1:]
        return strcpy
    else:
        return str
