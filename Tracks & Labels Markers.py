import cv2
import cv2.aruco as aruco
import numpy as np
import os

def findArucoMarkers(img, markerSize=4, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)
    
    print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs, ids)


def main():
    cap = cv2.VideoCapture(0)

    while True:
        succuess, img = cap.read()
        findArucoMarkers(img)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

if __name__== "__main__":
    main()