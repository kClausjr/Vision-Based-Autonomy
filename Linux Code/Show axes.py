import cv2 as cv
import cv2.aruco as aruco
import numpy as np

# - Define Tag
id_to_find = 27
marker_size = 5.715 # - [cm]

# - Get the camera calibration path
calib_path = "Calibration/"
camera_matrix =  np.loadtxt(calib_path+'cameraMatrix.txt', delimiter=',')
camera_distortion = np.loadtxt(calib_path+'cameraDistortion.txt', delimiter=',')

# - 180 deg rotation matrix around the x axis
R_flip = np.zeros((3,3), dtype=np.float32)
R_flip[0,0] = 1.0
R_flip[1,1] = -1.0
R_flip[2,2] = -1.0

# - Define the aruco dictionary
arucoDict = aruco.Dictionary_get(aruco.DICT_4X4_250)
arucoParam = aruco.DetectorParameters_create()

# - Capture the videocamera
cap = cv.VideoCapture(0)
# - Set the camera size as the one it was calibrated with
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

while True:

    # - Read the camera frame
    ret, frame = cap.read()

    # - Convert in grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # - Find all the aruco markers in the image
    bboxs, ids, rejected = aruco.detectMarkers(image=gray, dictionary=arucoDict, parameters=arucoParam, cameraMatrix=camera_matrix, distCoeff=camera_distortion)

    if ids != None and ids[0] == id_to_find:
        # - ret = [rvec, tvec, ?]
        # - array of rotation and position of each marker in camera frame
        # - rvec = [[rvec_1], [rvec_2], ...] attitude of the marker respect to camera frame
        # - tvec = [[tvec_1], [tvec_2], ...] postion of marker in camera frame
        ret = aruco.estimatePoseSingleMarkers(bboxs, marker_size, camera_matrix, camera_distortion)

        # - Unpack the output, get only the first
        rvec, tvec = ret[0][0,0,:], ret[1][0,0,:]

        # - Draw the detected marker and put a reference frame over it
        aruco.drawDetectedMarkers(frame, bboxs)
        aruco.drawAxis(frame, camera_matrix, camera_distortion, rvec, tvec, 10)

    # - Display the frame
    cv.imshow('frame', frame)

    # use 'x' to quit
    if cv.waitKey(1) & 0xFF == ord('x'):
        cap.release()
        cv.destroyAllWindows()
        break        