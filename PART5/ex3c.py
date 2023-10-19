#!/usr/bin/env python3

import cv2
import argparse
from functools import partial

def onTrackbar(image_gray, val, *args):
    _, thresh = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow('window - Ex3a', thresh)

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("({}, {})".format(x, y))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('window - Ex3a')
    cv2.imshow('Original', image)
    onTrackbar(image_gray, 100, 'window - Ex3a')

    cv2.createTrackbar('Threshold', 'window - Ex3a', 0, 255, partial(onTrackbar, image_gray))

    cv2.setMouseCallback('window - Ex3a', onMouse) 

    cv2.waitKey(0)

if __name__ == "__main__":
    main()
