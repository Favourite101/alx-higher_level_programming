#!/usr/bin/python3
def multiple_returns(sentence):
    num = len(sentence)
    if num == 0:
        fir = None
    else:
        fir = sentence[0]
    return num, fir
