#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    status = False
    try:
        print("{:d}".format(value))
        status = True
    except Exception as excp:
        sys.stdout = sys.stderr
        print(f"Exception: {excp}")
    finally:
        sys.stdout = sys.__stdout__
        return status
