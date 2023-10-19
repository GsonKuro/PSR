#!/usr/bin/env python3

import cv2
import argparse

def main():

    # Define variable to process commands
    parser = argparse.ArgumentParser(description='Script to compute prime numbers')
    # Add argument to choose max number to evaluate 
    parser.add_argument('-fn', '--file_name', type=str, help='cenas e coisas', required=False, default="/home/kurostrife/PSR/PSR/PART5/atlascar.png")

    args = vars(parser.parse_args())

    print(args)

    image = cv2.imread(args["file_name"], cv2.IMREAD_COLOR)

    cv2.imshow('Window', image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()