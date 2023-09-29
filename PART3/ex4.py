#!/usr/bin/env python3

import readchar

class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def addComplex(self,x):
        real = self.real + x[0]
        imaginary = self.imaginary + x[1]
    
    def multiplyComplex(self,x):
        real = self.real * y[0] + -(self.imaginary * y[1])
        imaginary = self.real * y[1] + self.imaginary * y[0]
    
    def __str__(self):
        print(self)
    
def main():
    print("Insert real and imaginary number, respetively, for first complex number")

    key1 = readchar.readkey()
    key2 = readchar.readkey()

    z1 = Complex(int(key1),int(key2))

    print("Insert real and imaginary number, respetively, for second complex number")

    key1 = readchar.readkey()
    key2 = readchar.readkey()

    z2 = Complex(int(key1),int(key2))

    print("Starting solving addition and multiplication")

    print(z1.addComplex(z2))
    print(z2.multiplyComplex(z2))

if __name__ == "__main__":
    main()