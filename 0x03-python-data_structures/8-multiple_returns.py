#!/usr/bin/python3
def multiple_returns(sentence):
    """Function returns a tuple with lenght of a string and first character."""
    length = len(sentence)
    if length > 0:
        string = length, sentence[0]
    else:
        string = length, None
    return string
