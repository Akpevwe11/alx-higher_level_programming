#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_element = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            printed_element += 1
        except Exception as e:
            pass
    print()
    return printed_element
