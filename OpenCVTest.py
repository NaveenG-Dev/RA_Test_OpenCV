# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 20:20:47 2020

@author: User
"""
import cv2 

#read the image and convert to gray image
image1 = cv2.imread('jointhold.jpg',cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('connector.jpg',cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread('paperclipB.jpg',cv2.IMREAD_GRAYSCALE)
image4 = cv2.imread('paperclipS.jpg',cv2.IMREAD_GRAYSCALE)
image5 = cv2.imread('jumpclipB.jpg',cv2.IMREAD_GRAYSCALE)
image6 = cv2.imread('jumpclipS.jpg',cv2.IMREAD_GRAYSCALE)

#Get the test image name
Test = input("Please enter the test image name: ")
image = cv2.imread(Test+'.jpg',cv2.IMREAD_GRAYSCALE)

#Get binary image
_,image1 = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY)
_,image2 = cv2.threshold(image2, 128, 255, cv2.THRESH_BINARY)
_,image3 = cv2.threshold(image3, 128, 255, cv2.THRESH_BINARY)
_,image4 = cv2.threshold(image4, 128, 255, cv2.THRESH_BINARY)
_,image5 = cv2.threshold(image5, 128, 255, cv2.THRESH_BINARY)
_,image6 = cv2.threshold(image6, 128, 255, cv2.THRESH_BINARY)
_,image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

#Get comparison loss value
ret1 = cv2.matchShapes(image1,image,cv2.CONTOURS_MATCH_I2,0.0)
ret2 = cv2.matchShapes(image2,image,cv2.CONTOURS_MATCH_I2,0.0)
ret3 = cv2.matchShapes(image3,image,cv2.CONTOURS_MATCH_I2,0.0)
ret4 = cv2.matchShapes(image4,image,cv2.CONTOURS_MATCH_I2,0.0)
ret5 = cv2.matchShapes(image5,image,cv2.CONTOURS_MATCH_I2,0.0)
ret6 = cv2.matchShapes(image6,image,cv2.CONTOURS_MATCH_I2,0.0)

#To find the lowest loss value
low = min(ret1,ret2,ret3,ret4,ret5,ret6)

# #To print the prediction
if low == ret1:
    print("Joint Hold")
elif low == ret2:
    print("Connector")
elif low == ret3:
    print("Big Paperclip")
elif low == ret4:
    print("Small Paperclip")
elif low == ret5:
    print("Big Jumpclip")
elif low == ret6:
    print("Small Jumpclip")






