#!/usr/bin/python3
def fizzbuzz():
    fz = ''
    for i in range(1, 101):
        if (i % 15 == 0):
            fz = 'FizzBuzz'
        elif (i % 5 == 0):
            fz = 'Buzz'
        elif (i % 3 == 0):
            fz = 'Fizz'
        else:
            fz = i
        print(fz, end=' ')
