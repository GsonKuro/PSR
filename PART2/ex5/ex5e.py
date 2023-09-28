#!/usr/bin/env python3

import readchar

def countNumberUpTo(stop_char):
    total_number = 0
    total_others = 0

    print('Start typing')

    inputs_other = []

    while True:
        key = readchar.readchar()

        input = key

        inputs_other.append(input)

        inputs_num = [item for item in inputs_other if item.isnumeric()]

        print(inputs_num)
        print(inputs_other)

        if input == stop_char:
            break

    for input in inputs_num: 
        total_number += 1
    for input in inputs_other:
        if not input.isnumeric():
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