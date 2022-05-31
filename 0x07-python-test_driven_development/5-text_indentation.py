#!/usr/bin/python3


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newtext = text.strip( )

    for delim in newtext:
        if delim == '.' or delim == '?' or delim == ':':
            print(delim)
            print('\n', end= '')
        print(delim, end= '')
