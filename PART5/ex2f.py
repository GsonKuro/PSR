#!/usr/bin/env python3

import cv2
import time
import argparse
import numpy

def main():

    image_rgb = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlas2000_e_atlasmv.png", cv2.IMREAD_COLOR)

    mask = cv2.inRange(image_rgb, (0,70,0), (55,255,60))

    indices = numpy.where(mask == 255)

    image_rgb[indices[0], indices[1], :] = [0,0,255]


    cv2.imshow("original", image_rgb)
    cv2.imshow("mask", mask)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()