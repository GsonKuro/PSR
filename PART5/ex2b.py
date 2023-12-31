#!/usr/bin/env python3

import cv2
import time
import argparse
import numpy

def main():

    image = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlascar.png", cv2.IMREAD_COLOR)

    print(type(image))
    print(image.shape)
    print(image.dtype)

    retval, image_thresholded = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    image_thresholded = image > 128

    cv2.imshow('Window', image_thresholded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()