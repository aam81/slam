#!/usr/bin/env python
import cv2
from display import Display
from extractor import Extractor

W = 1920//4
H = 1080//4

disp = Display(W, H)
fe = Extractor()

def process_frame(img):
    img = cv2.resize(img, (W, H))

    matches = fe.extract(img)
    if matches is None:
        return

    print(f"{len(matches)} matches")

    for pt1, pt2 in matches:
        u1,v1 = map(lambda x: int(round(x)), pt1.pt)
        u2,v2 = map(lambda x: int(round(x)), pt2.pt)
        cv2.circle(img, (u1,v1), color=(0,255,0), radius=3)
        cv2.line(img, (u1,v1), (u2,v2), color=(255,0,0))
    
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

i=0
while cap.isOpened():
    i = i+1
    if i>1000: break
    ret, frame =  cap.read()
    if ret == True:
        process_frame(frame)
    else:
        break