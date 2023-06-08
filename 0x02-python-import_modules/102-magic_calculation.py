#!/usr/bin/python3

def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for num in range(4, 6):
            c = add(c, num)
            return(c)
        else:
            return(sub(a, b))
