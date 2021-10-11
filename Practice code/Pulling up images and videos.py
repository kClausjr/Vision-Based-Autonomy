import cv2
# Part 1 - for a photo
# img = cv2.imread('Photos/IMG_0247.jpg')

# cv2.imshow('Cat', img)

#cv2.waitKey(0)

# Part 2 - for a video
capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

    capture.release()
    cv2.destoryAllWindows()