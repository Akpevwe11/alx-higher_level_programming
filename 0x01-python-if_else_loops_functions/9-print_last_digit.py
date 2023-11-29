#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_dig = number % -(10)
        print(-(last_dig), end='')
    else:
        last_dig = nm % 10
        print(last_dig, end='')
    return abs(last_dig)
