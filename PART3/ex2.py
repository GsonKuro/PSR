#!/usr/bin/env python3

import readchar

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

    z1 = complex(int(key1),int(key2))
    printComplex(z1)

    print("Insert real and imaginary number, respetively, for second complex number")

    key1 = readchar.readkey()
    key2 = readchar.readkey()

    print("Starting calculating addition and multiplication")

    z2 = complex(int(key1),int(key2))
    printComplex(z2)

    cenas = addComplex(z1,z2)
    print(cenas)
    coisas = multiplyComplex(z1,z2)
    print(coisas)
    printComplex(multiplyComplex(z1,z2))

if __name__ == "__main__":
    main()