#!/usr/bin/env python3

import cv2
import argparse
import numpy
from functools import partial

def main():

    #---------------------------------------------
    #           Initialization
    #---------------------------------------------

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    cv2.namedWindow('window')

    #---------------------------------------------
    #           Execution
    #---------------------------------------------

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)
    h,w,nc = image.shape

    xc = int(w/2)
    yc = int(h/2)
    cv2.circle(image, (xc,yc), 5, (0,0,255), -1)

    cv2.putText(image, 'PSR', (50,100), 3, 3, (0,0,255), 2)


    #---------------------------------------------
    #           Visualization
    #---------------------------------------------

    cv2.imshow('Original', image)
    cv2.waitKey(0)

    #---------------------------------------------
    #           Termination
    #---------------------------------------------

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
