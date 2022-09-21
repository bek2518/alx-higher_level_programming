#!/usr/bin/python3
def remove_char_at(str, n):
    strn = ""
    for i in range(len(str)):
        if i != n:
            strn = strn + str[i]
    return (strn)
