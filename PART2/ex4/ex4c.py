#!/usr/bin/env python3

import readchar

def countNumberUpTo(stop_char):
    total_number = 0
    total_others = 0

    print('Start typing')

    keys = []

    while True:
        key = readchar.readchar()

        keys.append(key)

        print(keys)

        if key == stop_char:
            break

    for key in keys:
        if key.isnumeric(): 
            total_number += 1
        else:
            total_others += 1

    print('You entered ' + str(total_number) + ' number.')
    print('You entered ' + str(total_others) + ' others.')

def main():
    """
    Principle cicle
    Value   : Nothing
    Return  : Strings
    """

    print("Choose key to stop code")

    key = readchar.readkey()

    print('Choosed ' + key)

    countNumberUpTo(key)

if __name__ == "__main__":
    main()