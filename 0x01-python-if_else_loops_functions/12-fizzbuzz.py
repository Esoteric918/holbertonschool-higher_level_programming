#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if not num % 5 and not num % 3:
            print("FizzBuzz ", end='')
        elif not num % 3:
            print("Fizz ", end='')
        elif not num % 5:
            print("Buzz ", end='')
        else:
            print("{} ".format(num), end='')
