#!/usr/bin/env python3

import cv2

def main():
    image = cv2.imread('/home/kurostrife/PSR/PSR/PART5/atlascar.png', cv2.IMREAD_COLOR)

    print(cv2.__version__)

    cv2.imshow('Window', image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()