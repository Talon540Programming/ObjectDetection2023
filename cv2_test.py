import cv2

stream = cv2.VideoCapture(0)

while True:
    ret, img = stream.read()
    cv2.imshow('frame', img)