#!/usr/bin/python3
def safe_print_integer(value):
    int_val = False
    try:
        print("{:d}".format(value))
        int_val = True
    except Exception as e:
        pass
    return int_val
