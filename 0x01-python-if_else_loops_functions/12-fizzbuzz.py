#!/usr/bin/python3
def fizzbuzz():
    for m in range(1, 100 + 1):
        if m % 5 == 0 and m % 3 == 0:
            print("FizzBuzz", end=", ")
        elif m % 5 == 0:
            if m == 100:
                print("Buzz", end=" ")
            else:
                print("Buzz", end=", ")
        elif m % 3 == 0:
            print("Fizz", end=", ")
        else:
            print(m, end=", ")
