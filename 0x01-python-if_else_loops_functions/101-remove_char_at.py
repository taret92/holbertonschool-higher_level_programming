#!/usr/bin/python3
def remove_char_at(str, n):
    remove = ""
    for i in range(len(str)):
        if i == n:
            remove = remove.replace(str[i], "")
            continue
    else:
        remove = remove + str[i]
        return (remove)
