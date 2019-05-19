#!/usr/bin/env python

import cv2
import numpy as np
from display import Display

W = 1920//4
H = 1080//4

display = Display(W, H)

def process_frame(img):
    img = cv2.resize(img, (W, H))
    
    display.paint(img)
    # cv2.imshow("image", img)
    # print(img.shape)
    # print(img)
    # window.refresh()

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

i = 0
while cap.isOpened():
    if i >= 170:
        break
    else:
        i = i+1

    ret, frame =  cap.read()
    if ret == True:
        process_frame(frame)
    else:
        break

print("hello")
