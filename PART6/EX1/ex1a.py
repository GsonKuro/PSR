#!/usr/bin/env python3

import cv2
import argparse
from functools import partial

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    cv2.namedWindow('window - Ex3a')
    cv2.imshow('Original', image)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()
