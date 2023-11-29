#!/usr/bin/python3

def uppercase(str):
    for c in str:
        ch = c
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            ch = chr(ord('A') + (ord(ch) - ord('a')))
        print("{}".format(ch), end='')
    print()
