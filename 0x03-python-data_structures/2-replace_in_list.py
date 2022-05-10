#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx == 0 or idx > my_list:
        return (my_list)

    else:
        for idx in range(len(my_list)):
            if my_list[idx] == idx:
                my_list[idx] == element