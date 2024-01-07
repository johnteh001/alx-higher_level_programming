#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b, c, d = 0, 0, 0, 0
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            a = tuple_a[0]
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            b = tuple_b[0]
    if len(tuple_a) >= 2:
        a, c = tuple_a[0], tuple_a[1]
    if len(tuple_b) >= 2:
        b, d = tuple_b[0], tuple_b[1]
    add_t = a + b, c + d
    return add_t
