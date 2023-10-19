#!/usr/bin/env python3

import cv2
import numpy
import argparse

# Global variables
val = 200
window_name = 'window - Ex3a'
image_gray = None

def onTrackbar(val):

    _,thresh = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, thresh)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    cv2.imshow('Original', image)

    global image_gray

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow(window_name)

    cv2.createTrackbar('Threshold', window_name, 0, 255, onTrackbar)

    # setting position of 'G' trackbar to  
    cv2.setTrackbarPos('Threshold', window_name, val) 

    onTrackbar(val)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()