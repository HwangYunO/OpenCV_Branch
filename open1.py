import cv2

def gsv(src) :
    dest = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    return dest

def binary(src) :
    dest = src.copy()
    _, dest = cv2.threshold(dst3, 127, 255, cv2.THRESH_BINARY)
    return dest
