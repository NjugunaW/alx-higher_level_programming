#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    frsh_lst = []

    for x in range(list_length):
        try:
            frsh_lst.append(my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            frsh_lst.append(0)
            print('division by 0')
            continue
        except IndexError:
            frsh_lst.append(0)
            print('out of range')
            continue
        except TypeError:
            frsh_lst.append(0)
            print('wrong type')
            continue
        finally:
            pass

    return frsh_lst
