#!/usr/bin/env python3

import argparse

# Funç~ao para descobrir números primos
from primo import isPrime

# maximum_number = 50

# Função para indicar qual número é primo
def main():
    """
    Ciclo principal 
    value   :   
    return  :   String
    """

    # Define variable to process commands
    parser = argparse.ArgumentParser(description='Script to compute prime numbers')
    # Add argument to choose max number to evaluate 
    parser.add_argument('-mn', '--maximum_number', type=int, help='max number.', required=False)
    # Add argument to say which person is saying hello 
    parser.add_argument('-n', '--name', type=str, help='Name person', required=False, default= 'Goncalo')
    # Add argument that obligates user to say hello
    parser.add_argument('-sh', '--say_hello', help='Say hello', action='store_true')

    # Create a dictionary
    args = vars(parser.parse_args())
    print(args)

    if args['say_hello']:
        print('Hi ' + args['name'] + ' !?!')

    print("Starting to compute prime numbers up to " + str(args['maximum_number']))

    for i in range(2, args['maximum_number']+1):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()