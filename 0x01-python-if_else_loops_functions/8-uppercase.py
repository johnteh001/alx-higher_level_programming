#!/usr/bin/python3
def uppercase(s):
    for char in s:
        upper_char = chr(ord(char) - 32) if ord('a') <= ord(char) <= ord('z') else char
        print("{}".format(upper_char), end="")
    print()

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
