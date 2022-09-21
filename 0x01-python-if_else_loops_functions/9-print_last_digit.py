#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number = number % 10
    elif number <= 0:
        number = (((number * -1) % 10) * -1)
    return (number)
