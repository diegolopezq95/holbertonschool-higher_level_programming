#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_s = (sentence)
    length = len(sentence)
    if not sentence: 
        return (length, tuple_s[0:1])
    else:
        return None
