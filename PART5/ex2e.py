#!/usr/bin/env python3

import cv2
import time
import argparse
import numpy

def main():

    image_rgb = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlas2000_e_atlasmv.png", cv2.IMREAD_COLOR)

    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(image_hsv, (50,170,50), (150,255,255))

    cv2.imshow('Original', image_hsv)
    cv2.imshow('Mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()