import cv2
import numpy as np
img = cv2.imread('502_0057_3.tif')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_val = np.array([0,0,0])
upper_val = np.array([0,0,0])

mask = cv2.inRange(hsv, lower_val, upper_val)
#to musze zapisac
mask_inv = cv2.bitwise_not(mask)
small = cv2.resize(mask_inv, (0,0), fx=0.25, fy=0.25, interpolation=cv2.INTER_LINEAR) 


rotate_90 = cv2.rotate(small,cv2.ROTATE_90_CLOCKWISE)

#tutaj zapisuje obrazek

inverted = np.invert(rotate_90)

import cv2

image = cv2.imread("mask.png")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
blurred = cv2.GaussianBlur(rgb, (3, 3), 0)

edged = cv2.Canny(blurred, 10, 100)

cv2.imshow("Original image", image)
cv2.imshow("Edged image", edged)
cv2.waitKey(0)




cv2.imwrite('mask.png', inverted)





