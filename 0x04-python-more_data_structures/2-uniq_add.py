#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    res = 0
    for i in my_list:
        if i in new_list:
            pass
        else:
            res += i
            new_list.append(i)
    return res
