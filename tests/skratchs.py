#!/usr/bin/env python3


import numpy as np
import cv2

a = [[100, 100], [200, 200]]

path = '/home/asak/dev_ws2/the_map.png'
img = cv2.imread(path)

cv2.line(img, a[0], a[1], (0,100,0), 2)


# Display the image
cv2.imshow('Line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()