import numpy as np
import cv2
def cnt(x):
	image1 = cv2.imread(x)
	imgray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#aprint(imgray)

#cv2.imshow('image',imgray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
	ret, thresh = cv2.threshold(imgray, 127, 255, 0)
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(imgray, contours, -1, (0,255,0), 3)
	cv2.imwrite('newout.png', imgray)


#	cv2.imshow('image',imgray)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()