#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
lastDigit = "Last digit of {} is {} and"
less = "is less than 6 and not 0"
greater = "is greater than 5"

if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

if last_digit < 6 and last_digit != 0:
    print(lastDigit.format(number, last_digit), less)
elif last_digit > 5:
    print(lastDigit.format(number, last_digit), greater)
else:
    print(lastDigit.format(number, last_digit), "is 0")
