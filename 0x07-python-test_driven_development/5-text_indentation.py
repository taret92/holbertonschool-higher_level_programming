#!/usr/bin/python3


def text_indentation(text):

    newtext = text.strip( )

    for delim in newtext:
        if delim == '.' or delim == '?' or delim == ':':
            print(delim)
            print('\n', end= '')
        print(delim, end= '')
