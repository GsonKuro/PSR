#!/usr/bin/env python3

from math import sqrt
from colorama import Fore, Back, Style
from time import time, ctime, localtime

Max_num = 50000000

def sqtRoot():
    initTime = time()

    for i in range(1,Max_num):
        result = sqrt(i)

    endTime = time() - initTime

    print("Finished calculate " + str(Max_num) + " numbers")
    print(str(endTime) + "s needed")

def main():

    print(ctime())
    print("The program will start processing the " + str(Max_num) + " numbers")
    sqtRoot()

if __name__ == "__main__":
    main()