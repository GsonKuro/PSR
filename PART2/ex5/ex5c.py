#!/usr/bin/env python3

import readchar

def countNumberUpTo(stop_char):
    total_number = 0
    total_others = 0
    order = 0

    print('Start typing')

    inputs_num = []
    inputs_other = []
    inputs_dic = {}

    while True:
        key = readchar.readchar()

        input = key

        if input.isnumeric():
            inputs_num.append(input)
        else:
            inputs_other.append(input)
            inputs_dic[str(order)] = input
            order += 1

        print(inputs_num)
        print(inputs_other)
        print(inputs_dic)

        if input == stop_char:
            break

    for input in inputs_num: 
        total_number += 1
    for input in inputs_other:
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