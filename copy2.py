import cv2

def gray(scr) :
    dest = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    return dest
