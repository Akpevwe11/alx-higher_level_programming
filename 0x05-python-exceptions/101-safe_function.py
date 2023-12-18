#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    retult = None
    try:
        retult = fct(*args)
    except Exception as excp:
        sys.stdout = sys.stderr
        print(f"Exception: {excp}")
    finally:
        sys.stdout = sys.__stdout__
        return retult
