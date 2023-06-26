#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printd_elems = 0

    for a in range(x):
        try:
            if type(my_list[a]) is int and printd_elems != x:
                print('{:d}'.format(my_list[a]), end='')
                printd_elems += 1
        except TypeError:
            continue

    print()

    return printd_elems
