#!/usr/bin/env python3

import cv2
import time
import argparse
import numpy

def main():

    image_rgb = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlascar.png", cv2.IMREAD_COLOR)

    image_b, image_g, image_r = cv2.split(image_rgb)


    retval, image_b_thresholded = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    retval, image_g_thresholded = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    retval, image_r_thresholded = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)

    image_merge1 = cv2.merge([image_r,image_g,image_b])
    image_merge2 = cv2.merge([image_r_thresholded,image_g_thresholded,image_b_thresholded])

    cv2.imshow('Window', image_b_thresholded)
    cv2.imshow('cenas', image_g_thresholded)
    cv2.imshow('coisas', image_r_thresholded)
    cv2.imshow('cenas e coisas', image_merge1)
    cv2.imshow('bajoras', image_merge2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()