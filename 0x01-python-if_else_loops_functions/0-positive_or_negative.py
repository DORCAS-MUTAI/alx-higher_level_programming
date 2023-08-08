#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = int(input("Enter number: "))
if number > 1:
    print("Is positive")
elif number == 0:
    print("Is Zero")
else:
    print("Is negative")
