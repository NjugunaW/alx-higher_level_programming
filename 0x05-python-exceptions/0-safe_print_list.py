#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements = 0

    try:
        for el in my_list:
            if elements < x:
                print('{}'.format(my_list[elements]), end='')
                elements += 1

        print()
    except TypeError:
        pass
    finally:
        return elements
