#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
s1 = "and is greater than 5"
s2 = "and is less than 6 and not 0"
s3 = "and is 0"
s4 = f"Last digit of {number} is {last}"
if last > 5:
    print(f"{s4} {s1}")
elif last == 0:
    print(f"{s4} {s3}")
elif last < 6:
    print(f"{s4} {s2}")
