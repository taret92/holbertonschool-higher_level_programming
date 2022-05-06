#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys(argv)
    operators = "+, -, *, /"
    a = argv[1]
    b = argv[3]
    if args != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit (1)
    elif argv[2] != operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)
    elif argv[2] == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif argv[2] == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif argv[2] == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif argv[2] == '/':
        print(f"{a} / {b} = {div(a, b)}")
