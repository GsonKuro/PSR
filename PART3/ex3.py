#!/usr/bin/env python3

from collections import namedtuple

import readchar

Complex = namedtuple('Complex', ['real', 'imaginary'])

def addComplex(x,y):
    real =  x[0] + y[0]
    imaginary = x[1] + y[1]
    return Complex(real,imaginary)
    
def multiplyComplex(x,y):
    real = x[0] * y[0] + -(x[1] * y[1])
    imaginary = x[0] * y[1] + x[1] * y[0]
    return Complex(real,imaginary) 

def printComplex(x):
    print(x)

def main():
    print("Insert real and imaginary number, respetively, for first complex number")

    key1 = readchar.readkey()
    key2 = readchar.readkey()

    z1 = Complex(int(key1),int(key2))
    printComplex(z1)

    print("Insert real and imaginary number, respetively, for second complex number")

    key1 = readchar.readkey()
    key2 = readchar.readkey()

    z2 = Complex(int(key1),int(key2))
    printComplex(z2)

    print("Starting solving addition and multiplication")

    printComplex(addComplex(z1,z2))
    printComplex(multiplyComplex(z1,z2))

if __name__ == "__main__":
    main()