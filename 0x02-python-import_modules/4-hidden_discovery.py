#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    list_of_names = dir(hidden_4)

    for name in list_of_names:
        if "__" not in name[:2]:
            print("{:s}".format(name))
