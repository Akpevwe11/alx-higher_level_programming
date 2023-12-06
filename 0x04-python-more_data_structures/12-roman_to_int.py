#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total_val = 0
    prev = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if roman_numerals[roman_string[c]] >= prev:
                total_val += roman_numerals[roman_string[c]]
            else:
                total_val -= roman_numerals[roman_string[c]]
            prev = roman_numerals[roman_string[c]]
    return total_val
