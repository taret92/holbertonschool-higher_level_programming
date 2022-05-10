#!/usr/bin/python3
from asyncio.windows_events import NULL

def element_at(my_list, idx):

    if (idx < 0 or idx >= len(my_list)):
        return(None)
    else:
        return(my_list[idx])
