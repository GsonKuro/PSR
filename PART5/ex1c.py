#!/usr/bin/env python3

import cv2
import time
import argparse

def main():

    count = 0

    while True:
        image = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlascar.png", cv2.IMREAD_COLOR)
        cv2.imshow('Window', image)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

        image = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlascar2.png", cv2.IMREAD_COLOR)
        cv2.imshow('Window', image)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

        count += 1

        if(count == 5):
            break

        


if __name__ == "__main__":
    main()