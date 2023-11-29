#!/usr/bin/env python3
import cv2

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
  # get an image from the camera

    # add code to show acquired image
    while True:
        _, image = capture.read()

        cv2.imshow('Window', image)

        # add code to wait for a key press
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    main()