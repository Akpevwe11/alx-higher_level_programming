#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a >= 2:
        first_element_a = tuple_a[0]
        second_element_a = tuple_a[1]
    elif len_a == 1:
        first_element_a = tuple_a[0]
        second_element_a = 0
    elif len_a == 0:
        first_element_a = 0
        second_element_a = 0

    if len_b >= 2:
        first_element_b = tuple_b[0]
        second_element_b = tuple_b[1]
    elif len_b == 1:
        first_element_b = tuple_b[0]
        second_element_b = 0
    elif len_b == 0:
        first_element_b = 0
        second_element_b = 0

    result_tuple = (first_element_a + first_element_b, second_element_a + second_element_b)

    return result_tuple