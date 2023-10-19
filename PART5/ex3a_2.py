#!/usr/bin/env python3

import cv2
import numpy as np

value = 0
max_value = 255
src = None

def on_trackbar(p):
    global src
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, p, max_value, cv2.THRESH_BINARY)
    cv2.imshow("Thresh", thresh)

def main():
    global src
    src = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlascar.png", cv2.IMREAD_COLOR)  # Open a color image


    cv2.namedWindow("Window", cv2.WINDOW_AUTOSIZE)  # Create a window for display.
    cv2.imshow("Window", src)  # Show our image inside it.
    cv2.createTrackbar("Threshold", "Window", value, max_value, on_trackbar)
    cv2.waitKey(0)  # Waiting for a key press to keep the window open.

if __name__ == '__main__':
    main()
