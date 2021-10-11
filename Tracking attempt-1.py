import cv2
import cv2.aruco as aruco
import argparse
import imutils
import sys

ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to imput image containing ArUco marker")
ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORGINAL", help="type of ArUco marker to detect")
args = vars(ap.parse_args())
 
dictionary = aruco.Dictionary_get(aruco.DICT_4X4_250)

# print("[INFO] loading image...")
# image = cv2.imread('image')

# if dictionary.get(args["type"], None) is None:
   # print("[INFO] ArUco tag of '{}' is not supported".format(args["type"]))
   # sys.exit(0)

# print("[INFO] detecting '{}' tags...".format(args["type"]))

parameters = aruco.DetectorParameters_create()

print("[INFO] starting video stream...")
cap = cv2.VideoCapture(0)

(markerCorners, markerIds, rejectedCanidates) = aruco.detectMarkers(image, dictionary, parameters=parameters)

