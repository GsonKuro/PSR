#!/usr/bin/env python3

import cv2 
import numpy as np 

def main():

    image = cv2.imread("/home/kurostrife/PSR/PSR/PART5/atlascar.png", cv2.IMREAD_COLOR)

    # preprocess the image 
    gray_img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY) 

    # Applying 7x7 Gaussian Blur 
    blurred = cv2.GaussianBlur(gray_img, (7, 7), 0) 

    # Applying threshold 
    threshold = cv2.threshold(blurred, 0, 255, 
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] 

    # Apply the Component analysis function 
    analysis = cv2.connectedComponentsWithStats(threshold, 4, cv2.CV_32S) 

    (totalLabels, label_ids, values, centroid) = analysis 

    print("\nTotal labels\n")
    print(totalLabels)
    print("\nLabels ids\n")
    print(label_ids)
    print("\nValues\n")
    print(values)
    print("\nCentroids\n")
    print(centroid)

    # Initialize a new image to store 
    # all the output components 
    output = np.zeros(gray_img.shape, dtype="uint8") 

    # Loop through each component 
    for i in range(1, totalLabels): 
        
        # Area of the component 
        area = values[i, cv2.CC_STAT_AREA]
        print(area)
        print(i) 
        print(cv2.CC_STAT_AREA)
        
        if (area > 140) and (area < 400): 
            componentMask = (label_ids == i).astype("uint8") * 255
            output = cv2.bitwise_or(output, componentMask) 


    cv2.imshow("Image", image) 
    cv2.imshow('Thresh', threshold)
    cv2.imshow('Gray', gray_img)
    cv2.imshow('Blurred', blurred)
    cv2.imshow("Filtered Components", output) 
    cv2.waitKey(0)

if __name__ == "__main__":
    main()