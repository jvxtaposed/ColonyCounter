import numpy as np
from .cv2 import *
def cnt(x):
	image1 = cv2.imread(x)
	imgray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
	#imgray = (255-imgray)

	counter = 0
	ret, thresh = cv2.threshold(imgray, 127, 255, 0)
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


	for c in contours:
		hull = cv2.convexHull(c)
		if cv2.contourArea(c) < 150:
			counter += 1
			out = cv2.drawContours(imgray,[hull], -1, (0,255,0), 5)


	cv2.imwrite('web/static/images/newout.png', out)
	print(counter)
	#cv2.imshow('image',out)
	cv2.destroyAllWindows()
	return counter


	
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()