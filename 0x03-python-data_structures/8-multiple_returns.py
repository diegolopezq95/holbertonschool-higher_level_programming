#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        sentence[0] = None
        return (length, sentence[0])
    else:
        return (length, sentence[0])