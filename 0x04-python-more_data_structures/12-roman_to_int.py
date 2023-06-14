#!/usr/bin/python3

def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    roman_letters = list(roman_string.upper())
    result = 0
    prev_value = 0
    for letter in roman_letters:
        if letter in roman_numerals:
            result += roman_numerals[letter]
            if roman_numerals[letter] > prev_value:
                result -= prev_value * 2
             prev_value = roman_numerals[letter]
         else:
             return (0)
    return(result)
