#!/usr/bin/python3


from typing import final
from unittest import result


def safe_print_division(a, b):
    try:
        div = (a / b)
        print("{:d}".format(div), end="")
    except(ZeroDivisionError):
        result(None)
    finally:
        print("inside result: {:d}".format(div))
    return div
