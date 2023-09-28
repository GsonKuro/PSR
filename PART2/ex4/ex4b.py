#!/usr/bin/env python3

import readchar

def readAllUpTo(stop_char):

    print('Start typing')

    keys = []

    while True:

        key = readchar.readkey()

        keys.append(key)

        print(keys)

        if(key == stop_char):
            break

def printAllCharsUpTo():
    """
    Print all chars 
    Stop_char   : Char choosed
    return      : Nothing
    """

    print("Commencing program please insert key")

    key = readchar.readkey()

    print("User pressed " + key)

    number = ord(key)

    chars = []

    for i in range(32, number):
        chars.append(chr(i))

    print(chars)

def main():
    """
    Principle cicle
    Value   : Nothing
    Return  : Strings
    """

    print("Choose key to stop code")

    key = readchar.readkey()

    print('Choosed ' + key)

    readAllUpTo(key)

    printAllCharsUpTo()

if __name__ == "__main__":
    main()