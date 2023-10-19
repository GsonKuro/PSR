#!/usr/bin/env python3

import cv2
import argparse
from functools import partial

def onTrackbar(image_hsv, min_B, max_B, min_G, max_G, min_R, max_R, *args):
    mask = cv2.inRange(image_hsv, (min_B,min_G,min_R), (max_B,max_G,max_R))
    cv2.imshow('window - Ex3a', mask)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    cv2.namedWindow('window - Ex3a')
    cv2.imshow('Original', image)
    onTrackbar(image_hsv, 0, 0, 0, 0, 0, 0)

    cv2.createTrackbar('min B/H', 'window - Ex3a', 0, 255, partial(onTrackbar, image_hsv))
    cv2.createTrackbar('max B/H', 'window - Ex3a', 0, 255, partial(onTrackbar, image_hsv))
    cv2.createTrackbar('min G/S', 'window - Ex3a', 0, 255, partial(onTrackbar, image_hsv))
    cv2.createTrackbar('max G/S', 'window - Ex3a', 0, 255, partial(onTrackbar, image_hsv))
    cv2.createTrackbar('min R/V', 'window - Ex3a', 0, 255, partial(onTrackbar, image_hsv))
    cv2.createTrackbar('max R/V', 'window - Ex3a', 0, 255, partial(onTrackbar, image_hsv))

    cv2.waitKey(0)

if __name__ == "__main__":
    main()
