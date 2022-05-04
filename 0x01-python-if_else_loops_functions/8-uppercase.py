#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii = ord(i)
        if ascii > 96 and ascii < 123:
            string = chr(ascii - 32)
        else:
            string = i
        print(f"{string}", end="")
    print("")
