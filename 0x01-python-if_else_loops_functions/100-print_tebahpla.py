#!/usr/bin/python3

letter = 0
for character in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(character - letter)), end="")
    letter =32 if letter == 0 else 0
