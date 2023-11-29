#!/usr/bin/python3
def remove_char_at(st, n):
    cpy_str = ""
    for i in range(len(st)):
        if i == n:
            continue
        else:
            cpy_str += st[i]
    return cpy_str
