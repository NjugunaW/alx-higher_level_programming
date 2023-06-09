#!/usr/bin/python3

def no_c(my_string):
    copy = [n for n in my_string if n != 'c' and n != 'C']
    return("".join(copy))
