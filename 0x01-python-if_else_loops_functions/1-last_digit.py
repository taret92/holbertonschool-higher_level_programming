#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = "Last digit of {} is {} and"
less = "is less than 6 and not 0"
greater = "and is greater than 5"

if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10
if number < 6 and last_digit != 0:
    print(last_digit.format(number, last_digit), less)
elif last_digit > 5:
    print(last_digit.format(number, last_digit), greater)
else:
    print(last_digit.format(number, last_digit), "is 0")
