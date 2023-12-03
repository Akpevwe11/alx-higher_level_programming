#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a >= 2:
        first_a = tuple_a[0]
        second_a = tuple_a[1]
    elif len_a == 1:
        first_a = tuple_a[0]
        second_a = 0
    elif len_a == 0:
        first_a = 0
        second_a = 0

    if len_b >= 2:
        first_b = tuple_b[0]
        second_b = tuple_b[1]
    elif len_b == 1:
        first_b = tuple_b[0]
        second_b = 0
    elif len_b == 0:
        first_b = 0
        second_b = 0

    result_tuple = (first_a + first_b,second_a + second_b)
                
    return result_tuple
