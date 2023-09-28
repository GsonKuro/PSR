#!/usr/bin/env python3

from collections import namedtuple

import readchar

Complex = namedtuple('Complex', ['r','i'])

def addComplex(x,y):  
    return x + y 
    
def multiplyComplex(x,y):
    return x * y

def printComplex(x):
    print(x)

def main():
    print("Insert real and imaginary number, respetively, for first complex number")

    key1 = readchar.readkey()
    key2 = readchar.readkey()

    _z1 = Complex(r = int(key1),i = int(key2))
    z1 = complex(_z1.r,_z1.i)
    printComplex(_z1)
    printComplex(z1)

    print("Insert real and imaginary number, respetively, for second complex number")

    key1 = readchar.readkey()
    key2 = readchar.readkey()

    print("Starting calculating addition and multiplication")

    _z2 = Complex(r = int(key1),i = int(key2))
    z2 = complex(_z2.r,_z2.i)
    printComplex(_z2)
    printComplex(z2)

    cenas = addComplex(z1,z2)
    print(cenas)
    coisas = multiplyComplex(z1,z2)
    print(coisas)
    printComplex(multiplyComplex(z1,z2))

if __name__ == "__main__":
    main()