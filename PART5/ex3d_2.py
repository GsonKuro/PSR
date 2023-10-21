#!/usr/bin/env python3

import cv2
import argparse
from functools import partial

def onTrackbar(image, use_hsv, min_B, max_B, min_G, max_G, min_R, max_R, _):
    if use_hsv:
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    else:
        image_hsv = image

    # Create a binary mask based on the specified color range
    mask = cv2.inRange(image_hsv, (min_B, min_G, min_R), (max_B, max_G, max_R))

    # Apply the mask to the original image
    segmented_image = cv2.bitwise_and(image, image, mask=mask)

    # Show the segmented image
    cv2.imshow('Segmentation', segmented_image)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    parser.add_argument('--hsv', action='store_true', help='Use HSV color space')
    args = parser.parse_args()

    # Load the image
    image = cv2.imread(args.image, cv2.IMREAD_COLOR)

    # Create a window for segmentation and trackbars
    cv2.namedWindow('Segmentation')

    # Create trackbars with functools.partial
    onTrackbarWithImage = partial(onTrackbar, image, args.hsv)
    cv2.createTrackbar('min B/H', 'Segmentation', 0, 255, onTrackbarWithImage, (0, 0, 0, 0))
    cv2.createTrackbar('max B/H', 'Segmentation', 0, 255, onTrackbarWithImage, (0, 255, 0, 255))
    cv2.createTrackbar('min G/S', 'Segmentation', 0, 255, onTrackbarWithImage, (0, 0, 0, 0))
    cv2.createTrackbar('max G/S', 'Segmentation', 0, 255, onTrackbarWithImage, (0, 255, 0, 255))
    cv2.createTrackbar('min R/V', 'Segmentation', 0, 255, onTrackbarWithImage, (0, 0, 0, 0))
    cv2.createTrackbar('max R/V', 'Segmentation', 0, 255, onTrackbarWithImage, (0, 255, 0, 255))

    # Initialize trackbar positions
    cv2.setTrackbarPos('max B/H', 'Segmentation', 255)
    cv2.setTrackbarPos('max G/S', 'Segmentation', 255)
    cv2.setTrackbarPos('max R/V', 'Segmentation', 255)

    # Display the initial image
    cv2.imshow('Segmentation', image)

    while True:
        key = cv2.waitKey(1)
        if key == 27:  # Press 'Esc' to exit
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()