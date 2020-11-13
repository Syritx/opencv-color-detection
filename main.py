import numpy as np
import cv2

def Loadimage(directory):

    image = cv2.imread(directory)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_colorRange = np.array([110,40,40])
    upper_colorRange = np.array([255,255,255])

    image_mask = cv2.inRange(hsv, lower_colorRange, upper_colorRange)
    cv2.imshow("Image mask", image_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Loadimage("test.png")