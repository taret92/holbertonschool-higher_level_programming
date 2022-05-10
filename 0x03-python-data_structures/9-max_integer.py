#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return (None)
    else:
        for i in my_list:
            if i < my_list[i]:
                max_value = my_list[i]
                return max_value
