#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence[0]:
        return (length, None)
    else:
        return (length, sentence[0])
