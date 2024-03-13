#!/usr/bin/python3
def uppercase(s):
    for char in s:
        uppercase_char = chr(ord(char) & 223)
        print(uppercase_char, end='')
    print()
