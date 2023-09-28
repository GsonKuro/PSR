#!/usr/bin/env python3

from primo import isPrime

maximum_number = 50

# Função para indicar qual número é primo
def main():
    """
    Ciclo principal 
    value   :   
    return  :   String
    """

    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()