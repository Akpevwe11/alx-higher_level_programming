#!/usr/bin/python3
def no_c(my_string):
    buffer = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        buffer += c
    return buffer
