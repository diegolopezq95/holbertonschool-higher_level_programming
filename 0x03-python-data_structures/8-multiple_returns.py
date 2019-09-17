#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_s = (sentence)
    length = len(sentence)
    if not sentence: 
        return None
    else:
        return (length, tuple_s[0:1])
